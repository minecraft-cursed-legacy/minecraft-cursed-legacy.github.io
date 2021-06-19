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
- the method is not static, because the TitleScreen.init method is not static.
- the method is private. This isn't a problem for instance methods, but if it were a static method, you would be required by mixin to make the INJECT method private
- The first parameters of the method are the parameters of the method we are injecting into. In this case, TitleScreen.init has no parameters, so we skip this step
- The last parameter of the method is a CallbackInfo, which has info about the mixin callback. If the method returned a value rather than being void, it would need to be a CallbackInfoReturnable instead.

## Making our mixin a bit more active

So, we want to actually do some stuff with our mixin, right? First of all, I will lay out what our tutorial mixin we are constructing in this section we will do. We will add a new button at the bottom of the title screen that exits the game. Simple, concise, and allows me to demonstrate some basic mixin concepts easily.

== Tutorial incomplete. It should be finished later this year. ==


{firstmod.html|Previous Tutorial} -- {index.html|Home}