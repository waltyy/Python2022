################
#IMPORT
################

#import all the functions from adventurelib
from adventurelib import *

################
#DEFINE ROOMS
################
Room.items = Bag()

start_room = Room("You wake in a dark farm. You need to turn on the generators to power the lights to see. There are a total of three generators to find. You can only walk forward")
chicken = Room("You are in a chicken coup, there are 4 exits. You hear spining blades to the NORTH of you. Type “look“ to look for exits")
beet = Room("You are in a beet farm, there are 3 exits. Type “look“ to look for exits")
potato = Room("You are in a potato farm, there are 3 exits. You hear spining blades to the WEST of you. Type “look“ to look for exits")
cow = Room("You are in a cow barn, there are 2 exits. Type “look“ to look for exits")
pig = Room("You are in a pigsty, there are 2 exits. You hear spining blades to the WEST of you. Type “look“ to look for exits")
gen_1 = Room("You are in the first generator room. You can pull a lever to turn on the generator. There are 2 exits. You hear spining blades NORTH of you. Type “look“ to look for exits")
gen_2 = Room("You are in the second generator room. You can pull a lever to turn on the generator. There are 2 exits. Type “look“ to look for exits")
gen_3 = Room("You are in the third generator room. You can pull a lever to turn on the generator. There are 2 exits. You hear spining blades NORTH of you. Type “look“ to look for exits")
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

lever_1 = Item("lever")
lever_1.description = "You see a lever on the generator"
lever_2 = Item("lever")
lever_2.description = "You see a lever on the generator"
lever_3 = Item("lever")
lever_3.description = "You see a lever on the generator"

################
#DEFINE BAGS
################

inventory = Bag()

################
#ADD ITEMS TO BAGS
################

inventory.add(lever_1)


################
#DEFINE ANY VARIABLES
################

lever_1_used = False
lever_2_used = False
lever_3_used = False
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
		current_room = chicken
	else:
		print("You cannot go this way")
	print(current_room)

@when("jump")
def jump():
	print("You have jumped")

@when("turn on lights")
@when("turn on lights")
def lights():
	print("It is too dark to see generators")

@when("go DIRECTION")
@when("walk DIRECTION")
@when("travel DIRECTION")
@when("e",direction = "east")
def travel(direction):

	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(current_room)
	else:
		print("You can't go this way")
	if current_room in [death_chicken,death_gen_1,death_gen_3]:
		quit()


@when("look")
def look():
	print("There are exits to the ",current_room.exits())

@when("use ITEM")
@when("pull ITEM")
def use(item):
	global lever_1_used,lever_2_used,lever_3_used
	if item in inventory and current_room == gen_1 and item == "lever":
		print("You pulled the lever on the generator")
		print("This generator is now running")
		gen_1.descrption = "This generator is currently running"
		lever_1_used = True

	elif item in inventory and current_room == gen_2 and item == "lever":
		print("You pulled the lever on the generator")
		print("This generator is now running")
		gen_2.descrption = "This generator is currently running"
		lever_2_used = True
	
	elif item in inventory and current_room == gen_3 and item == "lever":
		print("You pulled the lever on the generator")
		print("This generator is now running")
		gen_3.descrption = "This generator is currently running"
		lever_3_used = True

	else:
		print("You can't do that here")
		
	if lever_1_used == True and lever_2_used == True and lever_3_used == True:
		print("You have turned on all the generators. The lights start to flicker on. You see a door and run towards it. YOU WON!!!!!")
		quit()

@when("egg")
@when("easter egg")
@when("secret")
@when("russia")
@when("china")
def egg():
	print("Ha, imagine. This isn't Misha's game.")

@when("walk")
@when("run")
def walk():
	walk_die = input("Are you sure you want to walk into the great abyss?\n")
	if walk_die.lower() == "no":
		print("Sure no problem")
	else:
		print("You walked and tripped on a stone. You died lol")
		quit()

@when("hi")
@when("hello")
def hello():
	print("hi")


################
#MAIN FUNCTION
################

def main():
	print(current_room)
	start()

main()