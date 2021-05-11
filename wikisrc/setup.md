Setting up a Workspace | Minecraft Cursed Legacy Docs

This tutorial will guide you through setting up a workspace. It will not tell you how to install the Java Development Kit (JDK), or an IDE such as Eclipse or Intellij IDEA, as it is assumed you already have prior experience developing with java.

## Step 1

Firstly, clone the example mod, which can be found {https://github.com/minecraft-cursed-legacy/Example-Mod|here}. You can either download the example mod from github as a ZIP and extract it somewhere locally, or use Git to clone the repository.

## Step 2

Next, open the folder you have downloaded. Open the command prompt therein, and run one of these commands, depending on what IDE you use.

Note that you only need to run the rebuildLVT and genSources tasks when you use a new set of deobfuscation mappings, due to gradle caching the deobfuscated jars and sources jars. Therefore, provided you are using a plasma build you have used before, once you have already done this once, you will only need to provide the last parameter in the future.

### Eclipse


> ./gradlew rebuildLVT genSources eclipse


### Intellj IDEA


> ./gradlew rebuildLVT genSources idea


## Step 3

```
public class Test {
}
```

**hi**
