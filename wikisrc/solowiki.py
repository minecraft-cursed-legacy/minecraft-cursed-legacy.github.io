# Adapted from valoeghese/Solowiki to add code documentation functionality

import sys, os, shutil

if sys.version_info[0] < 3:
    raise Exception("Outdated Python Version! Must be using Python 3")

# CONSTANTS. Change these for input output dirs
# =========================================
INPUT_DIR = ""
OUTPUT_DIR = "../wiki/"
# =========================================

if len(sys.argv) < 2:
  print("Please specify the files to rebuild.")
  exit()

loadedBase = False
base0 = None
baseF = None
baseI = "        "
nextI = "  "

def loadBase():
  global loadedBase, base0, baseF
  
  if loadedBase:
    pass
  else:
    print("--- Loading template wiki-base.html")
    loadedBase = True
    with open("wiki-base.html") as baseSource:
      data = baseSource.read().split("<!--INJHERE-->")
      base0 = data[0]
      baseF = data[1]

def missingDirs(post): # create missing directories
  postc = ""
  for j in post.split("/")[:-1]:
    postc += "/" + j
  postc = postc[1:]
  
  try:
    os.makedirs(postc)
  except FileExistsError:
    pass

class Token:
  def __init__(self, dat, istext, opener, closer):
    self.data = dat
    self.text = istext
    if closer == None:
      self.tag = opener
    else:
      self.opener = opener
      self.closer = closer
  
  def getSimpleTag(self, effects):
    return self.tag
  
  def __str__(self):
    return self.data
    
  def __repr__(self):
    return self.__str__()

class LinkToken(Token):
  def __init__(self, dat, tagLink, tagImage):
    super().__init__(dat, False, tagLink, None)
    self.imgtag = tagImage
  
  def getSimpleTag(self, effects):
    return self.imgtag if effects.get(1, False) else super().getSimpleTag(effects)

HEADER = Token("/H1", False, "<h1>", "</h1>")
SUBHEADER = Token("/H2", False, "<h2>", "</h2>")
SUBHEADER_2 = Token("/H3", False, "<b>", "</b><br/>")
PARAHEADER = Token("/P", False, "<p>", "</p>")
BOLD = Token("/B", False, "<b>", "</b>")
ITALIC = Token("/I", False, "<i>", "</i>")
UNDERLINE = Token("/U", False, "<u>", "</u>")
QUOTE = Token("/BQ", False, "<div class=\"quote\">&nbsp;&nbsp;", "</div>")
LINK_START = Token("/LS", False, "<a href=\"", None)
IMAGE_START = Token("/IS", False, "<img src=\"", None)
LINK_MID = LinkToken("/LM", "\">", "\" alt=\"")
LINK_END = LinkToken("/LE", "</a>", "\"/>")
BREAK = Token("/NL", False, "<br/>", None)
RESET = Token("/R", False, None, None)
CODE_JAVA = Token("/SJ", False, "<pre><code class=\"language-java\">", "</code></pre></p>")

# Transpiling Lists
headers = [HEADER, SUBHEADER, SUBHEADER_2, QUOTE, PARAHEADER, CODE_JAVA]
wrappers = [BOLD, ITALIC, UNDERLINE, CODE_JAVA]
simple = [BREAK, IMAGE_START, LINK_START, LINK_MID, LINK_END]
# Tokenising Lists
tokenmap = {"**": BOLD, "''": ITALIC, "__": UNDERLINE, "!{": IMAGE_START, "{": LINK_START, "|": LINK_MID, "}": LINK_END, "```": CODE_JAVA}
greedytokens = [CODE_JAVA] # tokens that wait for their end and don't let others get in the middle.
greedytoken = None

# todo deduplicate code for token detection esp. greedy tokens
def processToken(currentRun, tokenList, forceToken):
  global tokenmap, greedytoken
  if (currentRun in tokenmap):
    if (greedytoken is None or currentRun == greedytoken): # check if the token in memory is greedy, and if it is, if we are allowed to end its contents (otherwise if not greedy this will also run)
      tokenList.append(addedToken := tokenmap[currentRun])
      
      if addedToken in greedytokens:
        greedytoken = currentRun if greedytoken is None else None
      return True
    elif forceToken: # if force token make a text token
      tokenList.append(Token(currentRun, True, None, None))
      return True
    else:
      return False
  else:
    for tokenkey in tokenmap:
      if currentRun.endswith(tokenkey):
        addedToken = tokenmap[tokenkey]
        
        if (greedytoken is None or currentRun == greedytoken): # check if the token in memory is greedy, and if it is, if we are allowed to end its contents (otherwise if not greedy this will also run)
          cutoffsize = len(tokenkey)
          tokenList.append(Token(currentRun[:-cutoffsize], True, None, None)) # add preceding text
          tokenList.append(addedToken) # add token
          
          if addedToken in greedytokens:
            greedytoken = currentRun if greedytoken is None else None
          return True
    if forceToken: # if force token make a text token
      tokenList.append(Token(currentRun, True, None, None))
      return True
    return False


for i in list(sys.argv)[1:]: # for each provided file
  print("Resolving " + i)
  inpt = INPUT_DIR + i
  try:
    mdFile = inpt.endswith(".md")
    if "." in inpt and not mdFile: # if an asset
      print("- File discovered to likely be an asset.")
      # asset nonsense
      if (os.path.exists(inpt)):
        print("--- Copying resource into bin.")
        outputpath = OUTPUT_DIR + i
        missingDirs(outputpath)
        shutil.copyfile(inpt, outputpath)
      else:
        print("--- Asset not present Skipping file.")
      continue #abuse the continue statement again
    with open(inpt if mdFile else (inpt + ".md")) as source:
      md = source.read().splitlines()
  except FileNotFoundError:
    print("- Markdown Source not found.")

    post = OUTPUT_DIR + (i[:-3] if i.endswith(".md") else i) + ".html"
    if os.path.exists(post):
      a = input("- Bin HTML file found. Permanently Delete file? [Y/N] ")
      if (a.upper() == "Y"):
        os.remove(post)
      print("--- Deleted file.")
    else:
      print("--- Bin does not exist, cannot act on the given file.")
    continue
  
  print("- Transpiling " + i)
  loadBase()

  metadata = md[0].split("|")
  base0Split = base0.split("<!--WIKINAMEHERE-->")
  
  if len(metadata) == 1:
    metadata.append("Unnamed Solowiki")
  
  html = base0Split[0] + metadata[1].strip() + base0Split[1] + "<span id=\"title\"><h1>" + metadata[0].strip() + "</h1></span>" + "\n"
  
  newLines = False
  tokens = []
  
  # Tokenise
  print("--- Tokenising")
  for line in md[1:]:
    line = line.strip()
    
    # Magic extra newline hack
    if line == "":
      if newLines:
        tokens.append(BREAK)
      newLines = True
      continue # yes I am abusing continue statement deal with it
    else:
      newLines = False
    
    # todo after making the code a bit cleaner and not a bodge, move this to a proper system like the wrappers, and move ``` to this
    if line.startswith("###"):
      tokens.append(SUBHEADER_2)
      line = line[3:].strip()
    elif line.startswith("##"):
      tokens.append(SUBHEADER)
      line = line[2:].strip()
    elif line.startswith("#"):
      tokens.append(HEADER)
      line = line[1:].strip()
    elif line.startswith(">"):
      tokens.append(QUOTE)
      line = line[1:].strip()
    elif not line.startswith("```") and greedytoken is None: # this hardcoding is why I want the code to be cleaner
      tokens.append(PARAHEADER)
    
    run = ""
    for char in line:
      run += char
      if run != "":
        if processToken(run, tokens, False):
          run = ""
    
    if run != "":
      processToken(run, tokens, True)
    
    tokens.append(RESET)

  # Parse Tokens into HTML
  print("--- Parsing to HTML")
  
  effects = {}
  
  html += baseI
  
  noNewLineNext = False # stupid hardcoded hackery because the codebase is already a massive mess. i will mark all parts of this hackery with the comment %dumbhack
  
  # Iterate over tokens
  for token in tokens:
    # Go through possible cases
    if token.text:
      html += token.data
    elif token in headers:
      wrapperToken = token in wrappers
      if wrapperToken and effects.get(hd, False):
         html += token.closer
         effects[token] = False
      else:
        html += token.opener
        effects[token] = True
        
        if wrapperToken: # %dumbhack
          noNewLineNext = True # %dumbhack
          continue # %dumbhack
    elif token == RESET:
      for hd in headers:
        if (hd not in wrappers) and effects.get(hd, False):
          html += hd.closer
          effects[hd] = False
      html += ("" if noNewLineNext else "\n") + ("" if effects.get(CODE_JAVA, False) else baseI) # contains some %dumbhack
    elif token in wrappers:
      if effects.get(token, False):
        html += token.closer
        effects[token] = False
      else:
        html += token.opener
        effects[token] = True
    elif token in simple:
      if effects.get(2, False): # not so simple now I guess. This is for image size stuff
        html += "\" width=\""
        effects[2] = False
      else:
        html += token.getSimpleTag(effects) # This method can be overrided. It is considered simple because it is a single tag, even if it changes on condition. Other tokens have a pair of tags.

        # Toggle Image Flag
        if token == IMAGE_START:
          effects[1] = True
        elif effects.get(1, False):
          if token == LINK_END:
            effects[1] = False
            effects[2] = False
          elif token == LINK_MID:
            effects[2] = True
    noNewLineNext = False
    
  
  # Finalise
  html += baseF
      
  post = OUTPUT_DIR + (i[:-3] if i.endswith(".md") else i) + ".html"
  missingDirs(post)
  
  bin = open(post, "w+")
  bin.write(html)
  bin.close()
  