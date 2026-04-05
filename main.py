from functions import *
from functions1 import *
clear()
spawn_drone(pumpkin)
for i in range(6):
	move(North)
spawn_drone(sunflower)
for i in range(2):
	move(East)
spawn_drone(default)