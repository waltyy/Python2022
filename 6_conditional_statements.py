
#Write a short program that asks the user how many ice creams they need. If they order more than 20, tell the user that there isn’t enough ice cream in stock.
icecream = int(input("How many ice creams do you want?\n"))
if icecream <= 20:
	print(f"Just to confirm, you are going to buy {icecream} ice creams")
elif icecream > 20:
	print(f"Sorry we do not have {icecream} ice creams in stock")
#Ask the user how far they intend to travel (just a number). If that number is greater than 200, remind the user to fill up with petrol before they leave
petrol = int(input("How far are you going to travel (just a number)\n"))
if petrol <= 200:
	print("Have a nice trip!")
elif petrol > 200:
	print("Don't forget to fill up with petrol before you leave")
#Write a short program that asks the user for their age. If their age is greater than or equal to 18, inform them that they are now considered an adult, otherwise, they are a minor.
age = int(input("How old are you?\n"))
if age <= 14:
	print("You are a child")
elif age <= 18:
	print("You are a teenager")
elif age <= 64:
	print("You are a adult")
elif age >= 64:
	print("You are a senior")
#Ask the user what their favourite movie is. If it is “Lord of the Rings”, tell them they have excellent taste, otherwise inform them that “Lord of the Rings” is clearly a superior film
movie = input("What is your favourite movie\n")
if movie.lower() == "lord of the rings":
	print("You have excellent taste")
else:
	print("Lord of the rings is clearly a superior film")
#Ask the user if they have heard the tale of Darth Plagueis the Wise. If they answer “no” or “No”, print out the tale of Darth Plagueis the Wise (google). If they answer anything else, say “You must be a fan?”
tale = input("Have you heard the tale of Darth Plagueis the Wise\n")
if tale.lower() == "no":
	print("The Tragedy of Darth Plagueis the Wise was a Sith legend that was relayed to Anakin Skywalker by Palpatine, telling of his master, Darth Plagueis. Plagueis, the legend went, was so powerful and so wise he could use the Force to influence the midi-chlorians to create life, and even save others from dying.")
else:
	print("You must be a fan?")
#Ask the user who directed “Passion of the Christ”. If they answer “Mel Gibson” say “correct”, otherwise, print out “Mel Gibson did”. Make sure your answer accepts any variation of Mel Gibson (eg mel Gibson, MEL GIBSON) etc. You can use string modifiers for this. (hint : you do not need to use or statements)
director = input("Who directed ""“Passion of the Christ”?\n")
if director.lower() == "mel gibson":
	print("Correct")
else:
	print("It was Mel Gibson")
#Create a variable called score and set it to zero. Write a short quiz program that asks the user 5 questions. If they get a question correct, increase the score by 1. At the end of the quiz, inform the user how many questions they got right. You may add more questions.
score = 0
print("Play this quiz!")
