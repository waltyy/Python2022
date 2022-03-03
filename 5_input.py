#Write code that asks the user to simply push any key, followed by enter
user_key = input("Simply push any key, then press enter\n")
print("You pressed", user_key)
#Ask the user to type their name and push enter
user_name = input("Please type your name\n")
print("Hello", user_name)
#Ask the user to type their age and push enter
user_age = input("How old are you?\n")
print("You are", user_age,"years old")
#Ask the user to type their name and store the response in a variable. Ask the user to type their age and store the response in a variable
print("You are", user_name,"and you are", user_age,"years old")
#Ask the user for their favourite movie and store it in a variable
user_movie = input("What is your favourite movie?\n")
#Ask the user for the name of a book and store it in a variable
user_book = input("What is the name of a book?\n")
#Ask the user for an adjective and store it in a variable
user_adjective = input("Name an adjective\n")
#Ask the user for a noun and store it in a variable
user_noun = input("Name a noun\n")
#Ask the user for a verb and store it in a variable
user_verb = input("Name a verb\n")
#Create 8 different print statements using one of the methods above to insert the variables into each string. Use multiple variables in each string.
print(f"I really like {user_book} it was quite {user_adjective}. Did you see the {user_noun}")
#Ask the user for their age and store it in a variable
age = int(input("How old are you again?\n"))
#Print out how old the user will be in 10 years
print(f"You will be {age+10} in 10 years")
#Print out the year that the user was born in (approximately, no need to consider months)
print(f"You were born in {2021-age}")
#Ask the user how many apples they have and store it in a variable
user_apples = int(input("How many apples do you have?\n"))
#Ask the user how many friends they have and store it in a variable
user_friends = int(input("How many friends do you have?\n"))
#Print out how many apples they can share equally amongst their friends, and how many apples they have left over (hint : use modulo and int division)
print(f"You can share {user_apples/user_friends} apples with your friends")