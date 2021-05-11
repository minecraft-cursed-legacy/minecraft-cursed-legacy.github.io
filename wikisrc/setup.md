Setting up a Workspace | Minecraft Cursed Legacy Docs

This tutorial will guide you through setting up a workspace. It will not tell you how to install the Java Development Kit (JDK), or an IDE such as Eclipse or Intellij IDEA, as it is assumed you already have prior experience developing with java.

## Step 1: Cloning the Example Mod

Firstly, clone the example mod, which can be found {https://github.com/minecraft-cursed-legacy/Example-Mod|here}. You can either download the example mod from github as a ZIP and extract it somewhere locally, or use Git to clone the repository.

## Step 2: Personalising the Mod Properties

Next, open the folder you have downloaded. 

Modify the ''gradle.properties'' file, and change the maven_group (usually your code package), archives_base_name (usually your mod id), and mod_version values to fit your mod.

## Step 3: Creating the Workspace

Open the command prompt in the folder you have downloaded, and run one of these commands, depending on what IDE you use.

Note that you only need to run the ''rebuildLVT'' and ''genSources'' tasks when you use a new set of deobfuscation mappings, due to gradle caching the deobfuscated jars and sources jars. Therefore, provided you are using a plasma build you have used before, once you have already done this once, you will only need to provide the last parameter in the future.

### Eclipse


> ./gradlew rebuildLVT genSources eclipse


### Intellj IDEA


> ./gradlew rebuildLVT genSources idea

## Step 4: Personalising the Workspace

Next, personalise the workspace. Because you're not gonna release your mod as "Example Mod" now, are you? This step is rather easy. Firstly, open the created project in your IDE. If you are using Intellij IDEA, I recommend changing the build path to build with IDEA instead of gradle.

There are three stages to refactoring the workspace:

### Refactor and Repackage Code.

Firstly, your IDE to refactor and repackage the example mod code to suit your needs. It is strongly recommended to keep the mixin classes their own subpackage called "mixin".

If your mod will not use mixins, you can delete the example mixin and ignore the stuff about mixin packages.

For example, if I were making a mod called "More Ores," I might want to change the root package to "com.example.moreores", rename the main class from "ExampleMod" to "MoreOres", and my mixin package would be "com.example.moreores.mixin".

### Edit the mixins json

If your mod does not use mixins, delete the example mixins json and skip this step.

Otherwise, secondly, edit the mixins json. Firstly, rename it to follow the standard provided pattern: "modid.mixins.json". For example, if I were making a "More Ores" mod, and my mod id were thus "more_ores", I would rename it to "more_ores.mixins.json". Then, you need to edit the "package" property within the json to match the new package you put your mixins in. For example, in the aforementioned "More Ores" mod, I would set it to "com.example.moreores.mixin"

### Edit fabric.mod.json

Finally, the mod properties. Inside your **src/main/resources** folder, locate the ''fabric.mod.json'' file. Change the relevant properties, such as mod name, authors, licence, and mod id. However, keep in mind the two most important things to change:

1. The "mixins" property. If you are not using mixins, delete this, otherwise change the value to specify the name you gave your mixin json.
2. The "entrypoints" property. Locate the "init" property inside of "entrypoints", and change the value to the fully qualified name of your main mod class. For example, in our hypothetical More Ores mod, it would be changed to "com.example.moreores.MoreOres".

## Step 5: Building the Mod.

You can build your mod at any time with the command:

> ./gradlew build

Your built mod jar will be found in the build/libs folder.
