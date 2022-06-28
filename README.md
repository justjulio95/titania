# Titania Space Shooter
#### Video Demo: https://youtu.be/4iYyXkEQIJ4
#### Description:

## Introduction
Titania is a project that was able to be brought to life through a long series of trial and error. I made it my mission to be able to build this simple game as best as I could while understanding the ins and outs of what I was writing out. In the process of creating this project, I took time to specifically study Python and Pygame and the ins and outs that go into creating a 2D project like this. While this is functionally a clone of the classic "Space Invaders" arcade game, my hope is to continue working on this project well after CS50 and develop it into a full fledged space-shooter or even a bullet-hell game.

## Modules
Titania is made of several different modules, all brought together to bring the project to life. They include alien.py, bullet.py, button.py, game_functions.py, game_stats.py, scoreboard.py, settings.py, ship.py, and the game itself titania.py.

###### alien.py
alien.py is a class that represents a single alien in the fleet of aliens shown in the game. In it there is code that establishes its image, its edges, and its movement. It inherits from the Sprite module provided by Python to assist in creating an entire fleet much easier, as well as keeping track exactly which aliens have been shot down in the list of aliens. 

###### bullet.py
bullet.py is a class that manages the bullets fired from the player ship. The module establishes the bullets hit box and its color, as well as manages the bullets velocity as its shot from the player ship.

###### button.py
button.py is a module that simply creates the "Play" button shown at the beginning of the game. In the module is code that assists in drawing the "Play" button to the screen, as well as establishing where it will appear and how big the button is. 

###### game_functions.py
game_functions.py is a module that essentially carries the bulk of the games work. In it is code written to check for a variety of events including user input, collisions, point scaling, and so on. This module is responsible for updating the game in real time, as well as managing all the few sounds heard in the game (laser fire, ship collision, and game over, for example). It is also responsible for creating the fleet of aliens that appears on screen, and getting the exact measurements to populate the screen accordingly. It also manages the fleets movement from left to right and the downward shift after each time the fleet hits the screens border.

###### game_stats.py
This module simply tracks the stats of the game - both dynamic and static stats. Upon every boot up of the game, the high scores and levels reset. This module also tracks when the game is in active status. 

###### scoreboard.py
scoreboard.py is responsible for the player hud. It draws to the screen the player's current score, their high score, the level they are on, and how many lives they have left. 

###### settings.py
The settings class establishes the settings (both static and dynamic) for Titania. In it you'll find the settings for the bullets width, color, the background color, the screen's dimensions, and the scale at which certain settings such as fleet and player movement speed will change. 

###### ship.py
The ship class helps in establishing a player object for the game. In it, are functions to assist in drawing the ship to the screen as well s updating it with every input the player may feed into the program. There's also a function called center_ship() which assists in recentering the ship every time the player dies. 

###### titania.py
This is where everything comes together. The main file of the game in which ll the modules and functions are fed into to make the game run the way it does. In it, I've created instances for settings, the ship (player), groups for the bullet class and enemy class, as well as created a flag for the game to check when it is active. When it is, the player will be able to enjoy the game. Otherwise, what should appear on the screen is a green button that reads "Play."