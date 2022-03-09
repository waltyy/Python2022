#the first two lines set up the context
#of the program and an initial state of
#the order_complete variable to false
#as well as an empty list for toppings
print("Hi, welcome to Ice Cream Maker")
order_complete = False
toppings_list = []
topping_count = 0

#the loop begins here and will complete
#when order_complete is no longer false
while order_complete == False:
	topping = input("What topping? - push enter to finish\n")
	if topping == "": #if the user pushes enter, the order is done
		print("Order Done")
		
		order_complete = True
	elif topping in toppings_list: #check if topping exists already
		print("You already have that topping")
	else: #add to list if not
		print("Great, adding it to the list")
		topping_count = topping_count + 1
		toppings_list.append(topping)

print("Here are your toppings")
#this next line might be new
#it joins the list together and seperates
#with commas, but you can change the seperator
print(",".join(toppings_list))