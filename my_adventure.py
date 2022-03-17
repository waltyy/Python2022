################
#IMPORT
################

#import all the functions from adventurelib
from adventurelib import *

################
#DEFINE ROOMS
################

start_room = Room("You wake in a dark farm, you can only walk forward")
chicken = Room("You are in a chicken coup, there are 4 exits. You hear spining blades infront of you. Type “look“ to look for exits")
beet = Room("You are in a beet farm, there are 3 exits. Type “look“ to look for exits")
potato = Room("You are in a potato farm, there are 3 exits. You hear spining blades to the left of you. Type “look“ to look for exits")
cow = Room("You are in a cow barn, there are 2 exits. Type “look“ to look for exits")
pig = Room("You are in a pigsty, there are 2 exits. You hear spining blades to the left of you. Type “look“ to look for exits")
gen_1 = Room("You are the first generator room, there are 2 exits. You hear spining blades infront of you. Type “look“ to look for exits")
gen_2 = Room("You are the second generator room, there are 2 exits. Type “look“ to look for exits")
gen_3 = Room("You are the third generator room, there are 2 exits. You hear spining blades infront of you. Type “look“ to look for exits")
death_chicken = Room("You have run into spinning blades. You have died!")
death_gen_1 = Room("You have run into spinning blades. You have died!")
death_gen_3 = Room("You have run into spinning blades. You have died!")

################
#DEFINE CONNECTIONS
################

start_room.north = chicken
beet.east = chicken
beet.north = potato
beet.west = gen_1
gen_2.west = chicken
gen_2.north = cow
potato.east = gen_3
pig.south = cow
chicken.north = death_chicken
gen_1.north = death_gen_1
potato.west = death_gen_1
gen_3.north = death_gen_3
pig.west = death_gen_3

################
#DEFINE ITEMS
################

Item.description = ""

lever_1 = Item
################
#DEFINE BAGS
################

################
#ADD ITEMS TO BAGS
################

################
#DEFINE ANY VARIABLES
################

current_room = start_room

################
#BINDS
################

@when("walk forward")
@when("go forward")
@when("forward")
def enter_chicken():
	global current_room
	if current_room == start_room:
		print("You are in the chicken coup")
		current_room = chicken
	else:
		print("You cannot go this way")
	print(current_room)

@when("jump")
def jump():
	print("You have jumped")

@when("go DIRECTION")
@when("travel DIRECTION")
@when("e",direction = "east")
def travel(direction):

	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(current_room)

@when("look")
def look():
	print(current_room)
	print("There are exits to the ",current_room.exits())

@when("use gen")
@when("use generator")


################
#MAIN FUNCTION
################

def main():
	print(current_room)
	start()

main()