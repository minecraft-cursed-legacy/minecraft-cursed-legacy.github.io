Your First Mixin | Minecraft Cursed Legacy Docs

Hello, again! Welcome to a tutorial on creating your first mixin for beta 1.7.3.

This tutorial will assume you {setup.html|already have a mod workspace set up}.

## So what is mixin, anyway?

Mixin is a framework that allows you to modify minecraft's source code using bytecode manipulation. It doesn't require you to know JVM bytecode to use it, but it's much easier if you have an understanding of how it works. Though that is beyond the purpose of this tutorial.

All mixins must be declared in your [modid].mixins.json file, as per the explanation on {setup.html|the setup page}, and as demonstrated in the example mod mixin.

## The Example Mod Mixin

Let's take a quick look at the Cursed Legacy Example Mod mixin:

```
@Mixin(TitleScreen.class)
public class ExampleMixin {
	@Inject(at = @At("HEAD"), method = "init()V")
	private void init(CallbackInfo info) {	
		System.out.println("This line is printed by an example mod mixin!");
	}
}
```

Woah woah, that's a lot to break down, so let's go through it step by step.

> @Mixin(TitleScreen.class)

This marker on the class tells mixin what code class we are injecting our code into. In this case, we are modifying the code of the title screen.

> @Inject(at = @At("HEAD"), method = "init()V")

This marker on the method tells mixin how we are modifying the code.

"@Inject" tells mixin we are injecting code into the game (as opposed to overwriting or modifying existing code).

"method = "init()V" tells mixin what method we are injecting into - that is, into the method called 'init' that takes no parameters and has a void return value. We could also just specify it as **method = "init"** in this instance, since there is only one method in that class with that name. However, if you are injecting into a method which shares its name with multiple other methods in that class, it is recommended to give mixin the full method signature.

"at = @At("HEAD")" tells mixin that our injection is to happen at the head of the method we are injecting into. That is, at the beginning of the method.

> private void init(CallbackInfo info)	

This format follows the standard for an INJECT mixin. Please Note the following:
- the method is void. INJECT mixin methods are not allowed to return a value.
- the "method" parameter of @Inject accepts the method signature. You can just put the method name here instead (e.g. "init") if it's not ambiguous
- the method is not static, because the TitleScreen.init method is not static.
- the method is private. This isn't a problem for instance methods, but if it were a static method, you would be required by mixin to make the INJECT method private
- The first parameters of the method are the parameters of the method we are injecting into. In this case, TitleScreen.init has no parameters, so we skip this step
- The last parameter of the method is a CallbackInfo, which has info about the mixin callback. If the method we are injecting into returned a value rather than being void, it would need to be a CallbackInfoReturnable instead.

Finally, let's take a brief look at the modid.mixins.json file in the example mod.

```
{
  "required": true,
  "package": "io.github.minecraftcursedlegacy.example.mixin",
  "compatibilityLevel": "JAVA_8",
  "mixins": [
  ],
  "client": [
    "ExampleMixin"
  ],
  "injectors": {
    "defaultRequire": 1
  }
}
```

There are three main things to note here:
- it's in the JSON data format
- you specify which package mixin should look in for mixins in the "package" field
- mixins are put by their class name in the "mixins" list. If it should only run on the client, we put it in "client" instead, and similarly, we can put it in a new list called "server" if it should only run on the server.

## Making our mixin a bit more active

So, we want to actually do some stuff with our mixin, right? First of all, I will lay out what our tutorial mixin we are constructing in this section we will do. We will add a new button at the bottom of the title screen that exits the game... in a fun way. Simple, concise, and allows me to demonstrate some basic mixin concepts easily.

First, let's add a button to the title screen. This should be pretty simple, just following what's in the vanilla TitleScreen class, we can add this to our "init" injection:

```
if (!this.minecraft.isApplet) {
	this.buttons.add(new Button(5, this.width / 2 - 100, this.height / 4 + 48 + 96, "Press Me (trust be bro)"));
}
```

The meaning of each parameter in Button can be determined by looking at how they're used in the Button class. The first parameter is the button id, then x, y, and the text to display.

"this.width / 2 - 100" gets us to start 100 units to the left of the centre, as the button is 200 units wide by default. The height is chosen as it should be 24 units below the previous buttons, which is the spacing in the vanilla title screen.

But hold on... WOAH, that's a LOT of errors we're getting there. Like, are you seeing me?

That's because although our code should be fine (as the contents of this method will just be injected), the java compiler doesn't know that. It thinks you're just writing a normal class, and in that case you've just referenced a whole bunch of fields that don't even exist! We can get around this by extending the same class that TitleScreen extends, since all these fields are just inherited by TitleScreen from that class.

When doing this in other mixins, you'll often be required to make a constructor, though this will just be discarded at compile time, so you can just let your IDE generate you one. An additional thing to note is if you extend an abstract class, you need to make your mixin class abstract as well. Neither of these apply in the case of our example mixin, fortunately for us.

```
@Mixin(TitleScreen.class)
public class ExampleMixin extends Screen {
```

Now that you extend Screen, you should see those errors go away. Great! The final thing I'd personally do here is change my mixin inject target from "HEAD" to "RETURN", to make sure my code runs after all the vanilla code. This isn't required, but unless you need your code to specifically run at another place in the method such as HEAD (which does happen quite often), it's good practise to run your code after vanilla code has already run.

The final thing to get this working is to make our button actually do something. Looking at the TitleScreen code, we see that vanilla handles button clicking in a method called "buttonClicked." Using our knowledge of inject mixins, we can easily append code for our button to the end of this. We set our button id as 5, so we'll check for that, and as for the "fun" way to exit the game... I think crashing the game is a fun way to go ;)

```
@Inject(at = @At("RETURN"), method = "buttonClicked")
private void onButtonClicked(Button button, CallbackInfo info) {
	if (button.id == 5) {
		throw new RuntimeException("Too Bad!");
	}
}
```

And that's it. You should have a button added to the title screen that crashes the game! Enjoy!

{firstmod.html|Previous Tutorial} -- {index.html|Home}