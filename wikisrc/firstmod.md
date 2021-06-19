Your First Mod | Minecraft Cursed Legacy Docs

Hello, again! Welcome to a tutorial on creating your first mod with fabric for beta 1.7.3 on Minecraft Cursed Legacy.

This tutorial will assume you {setup.html|already have a mod workspace set up}.

## Modifying the properties of the game!

To start, we will be editing the code in our mod's ModInitializer.

Let's start with a very simple mod, since it is our first mod, after all. We will modify the maximum stack size of sticks to be 8, so that players cannot have a stack with more than 8 sticks.

Change the code in your mod initialiser so that it adds this line:

```
ItemType.stick.setMaxStackSize(8);
```

So your mod initialiser's ''onInitialize'' method should look something like this:

```
@Override
public void onInitialize() {
    // whatever other initialisation code your mod has goes here
    ItemType.stick.setMaxStackSize(8); // set stick max stack size to 8
}
```

You can now run the modded game in your development environment through your IDE or ./gradlew runClient, and you should see that you can no longer stack sticks above a stack size of 8!

I'll go over this in detail, for those to whom this is not self explanatory:

- onInitialize() is called when the game first loads
- in this method, we access "ItemType.stick", which contains properties for the type of item known as "stick" (i.e. a stick)
- we invoke the setter for the max stack size on this item when we call ".setMaxStackSize(8)". This sets the properties for this type of item to have the maximum stack size of 8.

## Configuration

But what if we want our players to be able to configure the stack size?

No problem! We can use Cursed Legacy API's config library, which uses the ZoesteriaConfig library, to achieve this.

### Create a config template

Firstly, we want default values in case the value does not exist in the config yet or the config has not been created:

```
ConfigTemplate defaults = ConfigTemplate.builder()
  .addDataEntry("stick_stack_size", 8) // default max stack size of 8
  .build();
```

Then, we load or create the config:

```
Id configId = new Id("modid", "stack_sizes");
Container config = Configs.loadOrCreate(configId, defaults);
```

Now, we can modify our stack size modifying line to use the value configured:

```
ItemType.stick.setMaxStackSize(config.getIntegerValue("stick_stack_size"));
```

And now the default stick stack size should be 8, but it can be modified by changing the config! (albeit you have to restart the game for changes to apply)


{setup.html|Previous Tutorial} --  {index.html|Home} -- {firstmixin.html|Next Tutorial}