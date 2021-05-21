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

-- Tutorial to be continued later --
 