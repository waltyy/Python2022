#Write a list of the first 10 numbers in the Fibonacci sequence (google them if you need to). Print the list out
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(fibonacci)
#Write a list of your favourite fruits. Include at least 5 fruits. Print them out.
fruits = ["apple","bananna","watermellon","cucumber","plum"]
print(fruits)
#Write a list of youtubers that you watch. Include at least 4. Print them out.
youtubers = ["pewdiepie","seafog","stampy","white princet"]
print(youtubers)
#Create an empty list. On each line afterwards, add your favourite songs to the list. Add at least 5 songs. Print the list out when done.
songs = []
songs.append("Talk fast")
songs.append("Complete mess")
songs.append("505")
songs.append("Doin' time")
songs.append("Robbers")
print(songs)
#Create an empty list called books. Ask the user to add their top 5 favourite books to the list. Sort the list and print it out. (hint : you will need 5 input statements since loops have not yet been covered)
books = []
for i in range(0,5):
	user_books = input("Name a book\n")
	if user_books != "":
		books.append(user_books)
print(books)
#Create an empty list called pizza_toppings. Ask the user for up to 6 pizza toppings. If they enter nothing, do not add it to the list. Print out the final list of toppings
pizza_toppings = []
for i  in range (0,6):
	topping = input("Name a pizza topping\n")
	if topping != "":
		pizza_toppings.append(topping)
print(pizza_toppings)
#Create a list of fruits with at least 5 fruits already in the list. Ask the user for a fruit. If the fruit is not in the list, add it. If the fruit is in the list, inform the user and do not add the fruit. Print the list out at the end.

#Create a list of names. Sort the names and print them out. Reverse the list and print it out.

#Create a list that consists of the first 20 prime numbers (you can google them). Reverse this list. Print out the list. Print out the length of the list in a sentence using string formatting (eg “The Length of this list is 20 numbers long”).

#Create a list of common verbs. Sort the list. Print the list out.
