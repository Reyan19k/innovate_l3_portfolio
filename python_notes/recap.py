from ast import Num
import random
import string

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

# fav_games = [
#     "Farcry 3",
#     "The Outerworlds",
#     "Starwars Jedi: Fallen order"
# ]
# # print(fav_games)
# # fav_games [0] = "Farcry 6"
# # print(fav_games [0])
# # print(fav_games)

# # fav_games.append("Farcy 3")
# # print(fav_games)

# # fav_games.pop(0)
# # print(fav_games)

# for i in fav_games:
#     print(i)

# for i in range(2,10,1):
#     print(i)

# for i in range(10,-1,-1): # run the numbers backwardsby putting 10 as the strating point and -1(0) as the end point
#     print(i)

# num = 0

# while num < 10:
#     num +=1
#     print(num)

# my_num = 19
# computer_num = random.randint(1,50)

# while my_num != computer_num:
#     print(f"Number{my_num} and number {computer_num} do not match")
#     computer_num = random.randint(1,50)

# print(f"Number {my_num} and number {computer_num} match")

# welcome_msg = "Welcome to Code Nation"
# msg_length = print(len(welcome_msg))
# msg_length

# #part2 checking if odd or even
# name = "Welcome to code nation"
# length = len(name)%2
# # If a number has a remainder of 0 when divided by 2
# # the number is even.
# # If there is a remainder then it is odd.
# if length == 0:
#     print (name, "even")
# else:
#     print (name, "odd")

# welcome_msg = "Welcome to Code Nation"
# msg_length = len(welcome_msg)
# msg_length_even = len(welcome_msg)%2
# print(msg_length)
# if msg_length_even == 0:
#     print("The length of the welcome message is even")
# else:
#     print(welcome_msg)
#     print("Your message length isnt even")

# alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]
# for i in alpha:
#     print(i)

# user_num = int(input("Choose and number between 0 and 25: "))

# print(alpha[user_num], "is what your number represents in the alphabet")

#-----------------------------------------------------------------Example 2----------------------------------------------------------------------#

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]
for i in alpha:
    print(i)

answer = int(input ("Type a number to see the corresponding letter from the alphabet: "))
answer -=1
print(alpha[answer])