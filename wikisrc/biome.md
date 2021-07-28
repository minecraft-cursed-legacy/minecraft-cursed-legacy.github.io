Adding a Biome | Minecraft Cursed Legacy Docs

Welcome to the tutorial on adding a biome to beta minecraft with Minecraft Cursed Legacy using Cursed Legacy API!

This tutorial is split into 2 major sections: Creating the biome, and Making it generate in the world.

# 1. Creating the biome

## Biome Class

The first thing you are going to want is your biome class.

### The Basics
Make a class that extends Biome. In this you are going to want to create a constructor in order to set various properties of the biome, such as the name, and if it snows or is rainless. You can also edit the spawn lists: ''this.monsters'', ''this.creatures'', and ''this.waterCreatures
''. The spawn lists will have the normal creatures at their normal spawn rates by default.  

### Tree Types

If you want to change the kind of trees that generate, override the following method to return different tree features:
> public Feature getTree(Random random)

The default implementation generates oak trees, with one in ten trees being large oaks.

The various kinds of tree in vanilla minecraft are LargeOak (large oaks), OakTree (the small oaks), BirchTree, SpruceTree (the ones that look like christmas trees), and PineTree (the spruce wood trees that look like lollipop trees).

### Changing Biome Surface

You can change the surface blocks (by default grass and dirt) of the biome. All biomes have two fields: topTileId (the top tile, defaults to grass), and underTileId (the second layer, defaults to dirt). Change these fields, for example, in your constructor, to alter the surface of your biome. For example, you could make it sandy like a desert by adding this to your biome constructor:

```
this.topTileId = (byte)Tile.SAND.id;
this.underTileId = (byte)Tile.SAND.id;
```

### Note on Rainlessness

For some reason or another, the method for setting whether a biome is rainless is private, so access wideners / access transformers would need to be applied to that currently to make it accessible. A solution to this problem would be to override the canRain() method in your biome class and make it return false.

### Note on Grass and Foliage Colour
 
There are also unused grass and foliage colour properties. Knowledge of what these fields were intended to represent only comes from investigation of the colour values of the numbers and familiarity with biome code in later versions. Thus, setting these properties will not do anything, however it might still be useful in some cases to set them in case other mods wish to utilise them. This tutorial will ignore them, however, since they have no effect in the base game. For more information, please read the source code for ''Biome'' in your beta 1.7.3 workspace.

### Example Biome

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

## Cursed Legacy API Biome Extensions

Cursed Legacy API also offers more extensions to the biomes, and even more are to come in the future.

These are provided by implementing the interface **ExtendedBiome** on your biome class.

The example biome in this tutorial will implement ExtendedBiome and use the Cursed Legacy API Biome Extensions

```
public class SnowForest extends Biome implements ExtendedBiome {
```

### Changing Tree Density

You can set the number of trees per chunk by overriding this method from ExtendedBiome. This does not affect the extra tree that vanilla places in 1/10 chunks.

For example, in our Snow Forest biome, we want around 6 trees per chunk. Therefore we will add this code to the SnowForest biome class:

```
@Override
public int getTreesPerChunk() {
    return 6;
}
```

## Creating the Field

Next, you need to create a field to store your biome in somewhere. In this case we will just create it in our main class. This step is straightforward, as there is no registration for biomes in beta 1.7.3 minecraft.

In our example code, we will add our field in a new class called ModBiomes, however this field can be basically anywhere.

```
public class ModBiomes() {
    public static final Biome SNOW_FOREST = new SnowForest();
}
```

# 2. Adding the biome to the world

The Beta 1.7.3 biome generator uses temperature and humidity values to place biomes. Normally, the humidity is modified by the temperature via the expression "humidity = temperature * humidity," however we inject our modded biomes before this happens, allowing modders more freedom to place their biomes. You can perform this calculation yourself when placing your biome if you wish to be slightly more vanilla-like.

To add your biomes, add a listener to BiomePlacementCallback in your mod initialiser. This must be done at initialisation, otherwise you will need to manually force a biome array recalculation.

Using it, we can replace the biome for certain temperature ranges to get our desired effect.

Our example code:

```
BiomePlacementCallback.EVENT.register((temperature, humidity, biomeSetter) -> {
    if (temperature > 0.2f && temperature < 0.35f && humidity > 0.5f && humidity < 0.8f) {
        biomeSetter.accept(ModBiomes.SNOW_FOREST);
        return ActionResult.SUCCESS; // overwrite the biome with our custom one
    }

    return ActionResult.PASS; // delegate handling of the event to other mods, or fall back to vanilla behaviour
});
```

# Conclusion

Biomes in Beta 1.7.3 are very different to modern biomes, however, they are still easily added, and can be a great way to enhance the worldgen of worlds.


The example mod for the terrain module of Cursed Legacy API provides an excellent up-to-date reference on the biome generator. 
- {https://github.com/minecraft-cursed-legacy/Cursed-Legacy-API/blob/v1/legacy-terrain-v1/src/test/java/io/github/minecraftcursedlegacy/test/LevelGenTest.java#L39-L54|Relevant main class code.}
- {https://github.com/minecraft-cursed-legacy/Cursed-Legacy-API/blob/v1/legacy-terrain-v1/src/test/java/io/github/minecraftcursedlegacy/test/TestBiome.java|Relevant biome class code}

{tile.html|Previous Tutorial: Adding a Tile} -- {index.html|Home}

