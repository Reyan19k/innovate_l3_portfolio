import random

# print("this is my file")
# # = to comment

# greeting = "Hello World"
# # = = variable

# print(greeting)

# # Boolean = True or False
# print(True) # example of Boolean
# print(False) # example of Boolean
# # Interger = Whole number
# print(1234) # example of interger
# # Floating point = Numbers with decimal points
# print(12.34) # example of floating point
# # String = Characters
# print("This is a string for displaying character") # example of string
# # None = Nothing (place holder data)
# print(None) # example of None

# print(len(greeting))

# print(greeting[1])
# print(greeting[-1])

# print(greeting.upper())

# print("HELLO".lower())

# print("hello EVERYONE. THIS is innovate".capitalize())

# print("The quick brown fox fox fox".count("fox"))

# print("TheT quick brown fox".find("T"))

# print("The quick brown fox".replace("fox","frog"))

# print(len("The quick brown fox                         ".strip()))

# print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1,10))

# my_name = "Reyan"
# my_age = 23
# student = False

# print(my_name, my_age, student)

# print("My name is", my_name)
# print("I am", my_age, "years old.")
# print("I am a studen:", student)

# print("Hello my name is {} and I am {} years old".format(my_name,my_age)) # .format method, uses {} as placeholders
# print(f"Hello my name is {my_name} and I am {my_age} years old.") # f string method

# # Simple calculation methods
# print(1+2) # Addition
# print(6-4) # Subtraction
# print(6*6) # Multiplication
# print(5**5) # to the power of
# print(10/5) # Division
# print(20%2) # Modulas

# balance = 1000
# print(balance)
# amount = 500

# balance = amount+balance
# print(balance)

# answer = input("What is your name: ")
# print("Hello,", answer)

# music = "classical"

# if music == "classical":
#     print("Ah man, not again")
# elif music == "no music":
#     print("Put something on, please")
# else:
#     print("Volume up plaese")

# print(10%5==0)

# num = 50
# num2 = 100

# if num > num2:
#     print(f"{num} is bigger")
# elif num2 > num:
#     print(f"{num2} is bigger")
# else:
#     print("Bothe are equivalent")

# day = "saturday"

# if day == "saturday" or day == "sunday":
#     print("The weekend")
# else:
#     print("the weekday")

# def light_switch():
#     print("Lights on")

# light_switch()
# light_switch()

# def cash_with(amount,accnum):
#     print(f"You have withdrawn {amount} from {accnum}")

# cash_with(1000,56585485)

fav_games = [
    "Farcry 3",
    "The Outerworlds",
    "Starwars Jedi: Fallen order"
]
print(fav_games)
fav_games [0] = "Farcry 6"
print(fav_games [0])
print(fav_games)

fav_games.append("Farcy 3")
print(fav_games)

fav_games.pop(0)
print(fav_games)