################
#IMPORT
################

#import all the functions from adventurelib
from adventurelib import *

################
#DEFINE ROOMS
################

start_room = Room("You wake in a dark farm, you can only walk forward")
chicken = Room("You are in a chicken coup, there are 4 exits")
beet = Room("You are in a beet farm, there are 3 exits")
potato = Room("You are in a potato farm, there are 3 exits")
cow = Room("You are in a cow barn, there are 2 exits")
pig = Room("You are in a pigsty, there are 2 exits")
gen_1 = Room("You are the first generator room, there are 2 exits")
gen_2 = Room("You are the second generator room, there are 2 exits")
gen_3 = Room("You are the third generator room, there are 2 exits")
################
#DEFINE CONNECTIONS
################

################
#DEFINE ITEMS
################

################
#DEFINE BAGS
################

################
#ADD ITEMS TO BAGS
################

################
#DEFINE ANY VARIABLES
################

################
#BINDS
################

################
#MAIN FUNCTION
################

def main():
	start()

main()