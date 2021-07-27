Adding a Tile | Minecraft Cursed Legacy Docs

Welcome to the tutorial on adding an item to beta minecraft with Minecraft Cursed Legacy using Cursed Legacy API!

So, you want to add an item. This is a key part of development of many mods, as items are an incredibly useful way to interface with the player for various reasons (and also you probably want to have a ton of them anyway because you can)

Luckily, creating and registering items is incredibly simple.

## Step 1: The Item Type

First, create a field in your mod somewhere to store the item type.

```
public static ItemType myItem;
```

Then, create a class for your item type. A basic item type class might look like this:

```
public class BasicItemType extends ItemType {
  public BasicItemType(int id) {
    super(id);
  }
}
```

You may notice that beta 1.7.3 still uses integer ids. Luckily, you don't have to touch them yourself! Cursed Legacy API has a dynamic registry system that will allocate integer ids for you, and you can thus create a string identifier for your item instead.

Let's now register our item.
Initialise the field you created in your mod initialiser, like such: 

```
myItem = Registries.ITEM_TYPE.register(new Id("modid:my_item"), id -> new BasicItemType(id).setName("myItem"));
```

There's a lot going on there, so let's break it down a bit.

> new Id("modid:my_item")

This creates a string identifier with namespace "examplemod" (this should be your mod id), and name "my_item"

> id -> new BasicItemType(id).setName("myItem")

This is a lambda expression which first takes in the integer id provided by Cursed Legacy API's registries, and uses it to create an instance of the item type class we made. We then invoke the ''setName'' function on the item type to set the translation key for the item. In this case, the created translation key will be ''item.myItem.name''.

> Registries.ITEM_TYPE.register(...)

This is pretty self explanatory. This registers the item to Cursed Legacy API's dynamic registry system.

And congrats, that's all you need to add an item! But chances are you'd want a translated name and textures too, so let's briefly overview those.

## Translated Name

This is also extremely simple with Cursed Legacy API. Just add the following code to your mod initialiser:

```
Translations.addItemTranslation(myItem, "My Item");
```

The first parameter is the item to set the translated name of, and the second parameter is the name to set it as having.

## Item Texture

A simple 16x16 item texture can be easily applied to the using the 1.1.0 texture/model api (which uses chocohead's item atlas api under the hood for applying generated item models).

Simply create 4 nested folders in your src/main/resources directory: ''assets/modid/textures/item/'' (where modid is your mod id, as used in the id of the item). Inside the final "item" folder, put the 16x16 texture you want to use for the item, with the name as provided in your mod id (i.e. excluding the namespace). So for modid:my_item, the file name would be "my_item.png".

And that's it. You should have the item texture in game now!

## Final Notes and on Obtaining your Item

Obtaining your item could prove difficult if you don't have a creative-mode mod in your workspace, so a simple way to obtain your item for testing would be to add a simple recipe.

As an example, a simple shapeless recipe that takes 1 dirt and gives your item could be added as such:

```
Recipes.addShapelessRecipe(new ItemInstance(myItem), Tile.DIRT);
```

For further reference, check out {https://github.com/minecraft-cursed-legacy/Cursed-Legacy-API/tree/v1/legacy-textures-v1/src/test/|the texture api test mod}

{index.html|Home} -- {tile.html|Next Tutorial: Adding a Tile}
