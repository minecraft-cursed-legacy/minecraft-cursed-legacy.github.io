Creating a Worldtype | Minecraft Cursed Legacy Docs

Welcome to the tutorial of making a World Type using Cursed Legacy API!

This tutorial is INCOMPLETE and should be finished soon.

This tutorial is in 2 parts: creating a Chunk Generator (which goes over each part of chunk generation), and adding a world type.

# Creating a Chunk Generator

The first thing you will need is your own chunk generator. To do this, we can make a class extending ''ChunkGenerator'', a base for a worldgen LevelSource provided by Cursed Legacy API. Then, create a constructor matching super.

```
public class ExampleChunkGenerator extends ChunkGenerator {
  public ExampleChunkGenerator(Level level, long seed) {
    super(level, seed);
  }
}
```

Now it's time to get started with the actual worldgen! For the basic world type tutorial, we're gonna create a rather boring world with a random height each chunk. However in practise, if you want smooth terrain, you're going to want to initialise noise generator(s) in your constructor and use that to define the shape. However, that is beyond the scope of the tutorial.

## Chunk Shaping

The first method you're gonna want to implement is the ''shapeChunk'' method. This is what determines the initial shape of the chunk being generated, using stone, air, and water to specify where there's solids, air, and liquids. These "base blocks" used may differ in other dimensions (for example, the nether uses netherrack and lava instead of stone and water). The usual way to do this is to generate per column, or if you're doing linear interpolation of 3d noise like in vanilla, per each of a certain sized segment in the chunk. We'll do the former, so let's start by looping over each x,z position in the chunk. We only need the coördinates local to the chunk, and a chunk is 16x16 horizontally, so we can use these for loops:

```
for (int localX = 0; localX < 16; localX++) {
  for (int localZ = 0; localZ < 16; localZ++) {
  }
}
```

Now for some actual height calculations. As aforementioned, for the sake of an example, we will be giving each chunk a completely random height. So let's do that. We'll compute a random height betweek 61 and 71 before starting. The random number generator for the Chunk Generator has its seed set based off of x and z each time a chunk is generated (i.e. for shapeChunk, buildSurface, and generateCarvers), so we'll use that.

```
int height = this.rand.nextInt(11) + 61; // 61 + any number from 0-10.

for (int localX = 0; localX < 16; localX++) {
  for (int localZ = 0; localZ < 16; localZ++) {
  }
}
```

Then, for each block in the chunk (i.e. in the loops we've had), we'll go from the bottom of the world, y=0, up to the height we have calculated and set the position to stone. The tile array is full of id 0 (air) by default, as with a regular Java array. The final step is to add water if the heightmap goes below sea level. We will use sea level 63 as an example. The full method we have is thus:

```
@Override
protected void shapeChunk(int chunkX, int chunkZ, byte[] tiles, Biome[] biomes) {
  int height = this.rand.nextInt(11) + 61; // 61 + any number from 0-10.

  for (int localX = 0; localX < 16; localX++) {
    for (int localZ = 0; localZ < 16; localZ++) {
      for (int y = 0; y <= localHeight; y++) {
        tiles[getIndex(localX, y, localZ)] = (byte) Tile.STONE.id;
      }

      if (height < 63) {
        for (int y = 63; y > height; y--) { // fill blocks from y=63 to just above sea level with water when height dips below sea level
          tiles[getIndex(localX, y, localZ)] = (byte) Tile.STILL_WATER.id;
        }
      }
    }
  }
}
```

If you want to make the transitions between chunk heights more smooth, you could use averaging, or even interpolate between heights. However the best tool for creating a realistic looking heightmap is to use a form of gradient noise, which will be covered in a future tutorial.

## Surface Building (biome-specific blocks)

Coming Soon.

## Carver Generation

Now for Carver Generation, i.e. Caves. This is quite straightforward, as vanilla has the cave algorithm separated from chunk generation, and we can thus include it in directly in our chunk generator. Alternatively, you could use a custom carver, or the nether cave (provided your worldgen works with the nether cave).

Firstly, we are going to want to create a cave instance and store it in a field. This is pretty straightforward.

```
private final Cave cave = new OverworldCave();
```

Secondly, and finally, we can just override ''generateCarvers'' and call the cave's generate method from there:

```
@Override
protected void generateCarvers(int chunkX, int chunkZ, byte[] tiles, Biome[] biomes) {
  this.cave.generate(this, this.level, chunkX, chunkZ, tiles);
}
```

Now caves should be generating in your world!

## Changing Player Spawn Conditions

Coming Soon.

## Feature Placement

Coming Soon.

# Making the World Type

Coming Soon.

# Additional Resources

- {https://github.com/minecraft-cursed-legacy/Cursed-Legacy-API/tree/v1/legacy-worldtypes-v1/src/test/java/io/github/minecraftcursedlegacy/test|Cursed Legacy Worldtype API Tests}

{biome.html|Previous Tutorial: Adding a Biome} -- {index.html|Home}