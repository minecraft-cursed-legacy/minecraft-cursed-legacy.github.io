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

Next, personalise the workspace. Because you're not gonna release your mod as "Example Mod" now, are you? This step is rather easy. Firstly, open the created project in your IDE. If you are using Intellij IDEA, I recommend firstly changing the build path to build with IDEA instead of gradle.

There are three stages to refactoring the workspace:

### Refactor and Repackage Code.

Use your IDE to refactor and repackage the code.
