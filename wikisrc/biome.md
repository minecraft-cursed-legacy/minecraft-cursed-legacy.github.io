Adding a Biome | Minecraft Cursed Legacy Docs

Welcome to the tutorial on adding a biome to beta minecraft with Minecraft Cursed Legacy using Cursed Legacy API!

This tutorial is split into 2 major sections: Creating the biome, and Making it generate in the world.

## 1. Creating the biome

The first thing you are going to want is your biome class.

Make a class that extends Biome. In this you are going to want to create a constructor in order to set various properties of the biome, such as the name, and if it snows or is rainless. You can also edit the spawn lists: ''this.monsters'', ''this.creatures'', and ''this.waterCreatures
''. The spawn lists will have the normal creatures at their normal spawn rates by default.  

There are also unused grass and foliage colour properties. Knowledge of what these fields were intended to represent only comes from investigation of the colour values of the numbers and familiarity with biome code in later versions. Thus, setting these properties will not do anything, however it might still be useful in some cases to set them in case other mods wish to utilise them. This tutorial will ignore them, however, since they have no effect in the base game. For more information, please read the source code for ''Biome'' in your beta 1.7.3 workspace.

If you want to change the kind of trees that generate, override the following method to return different tree features:
> public Feature getTree(Random random)

The default implementation generates oak trees, with one in ten trees being large oaks.

The various kinds of tree in vanilla minecraft are LargeOak (large oaks), OakTree (the small oaks), BirchTree, SpruceTree (the ones that look like christmas trees), and PineTree (the spruce wood trees that look like lollipop trees).

For some reason or another, the method for setting whether a biome is rainless is private, so access wideners / access transformers would need to be applied to that currently to make it accessible. A solution to this problem would be to override the canRain() method in your biome class and make it return false.

The example biome will be called "Snow Forest," and be snowy, and have 1/3 of generated trees be spruce trees:

```
public class SnowForest extends Biome {
    public SnowForest() {
        this.setName("Snow Forest"); // set the name to "Snow Forest"
        this.setSnowy(); // set the biome to snow instead of rain
    }

    @Override
    public Feature getTree(Random random) {
        return random.nextInt(3) == 0 ? new SpruceTree() : super.getTree(random);
    }
}
```

Next, you need to create a field to store your biome in somewhere. In this case we will just create it in our main class. This step is straightforward, as there is no registration for biomes in beta 1.7.3 minecraft.

```
public static final Biome SNOW_FOREST = new SnowForest();
```

## 2. Adding the biome to the world


## Conclusion

I haven't finished this yet
In the meantime please reference the example biome code {https://github.com/minecraft-cursed-legacy/Cursed-Legacy-API/blob/v1/legacy-terrain-v1/src/test/java/io/github/minecraftcursedlegacy/test/LevelGenTest.java#L39-L54|here} and {https://github.com/minecraft-cursed-legacy/Cursed-Legacy-API/blob/v1/legacy-terrain-v1/src/test/java/io/github/minecraftcursedlegacy/test/TestBiome.java|here}

{tile.html|Previous Tutorial: Adding a Tile} -- {index.html|Home}

