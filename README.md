# This is no longer a Sonic the Hedgehog game in Pygame, it is a Super Sonic bossfight simulator.
Originally, this was a simple attempt at making a working Sonic game using Pygame. I've tried getting angled movement to work but it's actually quite troublesome. The angles did work to some extent but it was incredibly buggy and just not worth it, so I had switched to using Pygame.rect instead of pygame.mask for hitboxes. Eventually, I dropped it altogether since this is a school project and I wanted to upload a working game, not an attempt at making angled movement.

My tip to you is to use another engine for a Sonic game, preferably Godot or Gamemaker if you're a beginner, however if you insist on using Pygame, remember to use pygame.mask instead of traditional hitboxes with pygame.Rect.

I don't really care much about what happens to my code so feel free to use any of it, but please, credit me if you do use any of it.

# The original Sonic code has been commented out, so if you uncomment the Sonic class and the EggmanLand class, you can reprogram the game to run using those. If you do get angled movement working, let me know.

# Also if you get an error regarding PyTMX, install it with "pip install pytmx" in the terminal/command prompt.
