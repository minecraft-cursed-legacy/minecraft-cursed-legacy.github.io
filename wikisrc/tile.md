Adding an Item | Minecraft Cursed Legacy Docs

Welcome to the tutorial on adding a tile to beta minecraft with Minecraft Cursed Legacy using Cursed Legacy API!

Tiles, also known as "Blocks" in more modern versions of the game, are a key part of minecraft. From dirt to jukeboxes, logs to diamond ore, they form the world, and are the key means of interaction between the player and the world.

Luckily, creating and Registering custom Tiles with Cursed Legacy API is only slightly more complex than adding an item.

## Step 1: The Tile

First, as with the items, create a field in your mod somewhere to store the tile.

```
public static Tile myTile;
```

Then create a class for your tile. A basic tile class might look like this:

```
public class MyCustomTile extends Tile {
  public MyCustomTile(int id) {
    super(id, Material.ORGANIC);
    this.hardness(1.0f);
    this.sounds(GRASS_SOUNDS);
    this.name("myCustomTile");
  }
}
```

Let's go over what each part does.

> public MyCustomTile(int id)

We create a constructor that takes the internal integer tile id which will be provided by cursed legacy api's registries.

> super(id, Material.ORGANIC);

This id must be passed to the super constructor for tile, along with the material to which this tile belongs. In this example, I have picked Material.ORGANIC, which is used for leaves, grass, etc. 

> this.hardness(1.0f);

This sets the hardness of the tile to 1.0f. This affects the time it takes to mine, and the blast resistance.

> this.sounds(GRASS_SOUNDS);

This sets the sounds that this tile makes when walked on and broken/placed. In this case, we have picked the grass block sounds.

> this.name("myCustomTile");

This sets the name for the translation key. In this case, the generated translation key will be "tile.myCustomTile.name"

## Instantising and Registering the Tile

Let's now register the tile.
Initialise the field you created in your mod initialiser, like such: 

```
myTile = Registries.TILE.register(new Id("modid:my_tile"), MyCustomTile::new);
```

This is very similar to how registering an item works, which is broken down and explained in the previous tutorial. The key differences is that we are using the TILE registry, and because our tile's constructor directly matches the signature of the initialisation function, we can use a method reference instead of a normal lambda.

However, of course, a normal lambda would still work if you'd prefer: Registries.TILE.register(new Id("modid:my_tile"), id -> new MyCustomTile(id))

## Tile Item

Chances are, you want your tile to have an associated placeable item. This is not done automatically, and will need to be created separately. Luckily, Cursed Legacy API provides a method to do this in just one line!

```
TileItems.registerTileItem(new Id("modid:my_tile"), myTile);
```

The Id provided to the ''registerTileItem'' method should ideally be identical to the one you use for the tile, however, this is not required.

## Translated Name

This follows pretty simply from how you do it for items in the previous tutorial. We use addTileTranslation instead of addItemTranslation.

```
Translations.addTileTranslation(myTile, "My Tile");
```

The first parameter is the tile to set the translated name of, and the second parameter is the name to set it as having.

## Tile Texture

A simple 16x16 cube-all or cross texture can be easily applied to the using the 1.1.0 texture/model api. This api uses paulevs' {https://github.com/paulevsGitch/B.1.7.3-CoreLib|corelib} library under the hood to apply the detected models. If you're interested in making more complex models, or even using OBJ models, then you may be interested in learning how to use corelib directly.

To add a tile texture for a simple cube-all tile, make sure you have a set of nested folders in your src/main/resources directory with the structure: ''assets/modid/textures/tile/'' (where modid is your mod id, as used in the id of the tile). Inside the final "tile" folder, put the 16x16 texture you want to use for the item, with the name as provided in your mod id (i.e. excluding the namespace). So for modid:my_tile, the file name would be "my_tile.png".

This should be enough to add a basic cube-all texture!

This can be switched to a cross or grass-like texture shape by adding a relevant model file (check out the example texture-api mod, linked near the end of the page, to see how that is done).

## Final Notes and on Obtaining your Tile

Obtaining your item could prove difficult if you don't have a creative-mode mod in your workspace, so a simple way to obtain your item for testing would be to add a simple recipe.

As an example, a simple shapeless recipe that takes 1 sand and gives your tile could be added as such:

```
Recipes.addShapelessRecipe(new ItemInstance(myTile), Tile.SAND);
```

For further reference, check out {https://github.com/minecraft-cursed-legacy/Cursed-Legacy-API/tree/v1/legacy-textures-v1/src/test/|the texture api test mod}

{item.html|Previous Tutorial: Adding an Item} -- {biome.html|Next Tutorial: Adding a Biome}
