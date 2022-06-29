from ast import Break
import random
# print(int(5.4))
# print(int(5.9)) # aways rounds down
# print(int(round(5.9))) # use round() to round up
# print(int("54"))

# acc_balance = 1000

# deposit = int(input("How much would you like to deposit: "))

# acc_balance += deposit

# print(f"Your account balance is: {acc_balance}")


# print("What is your name")
# name = input()

# if name:
#     print(f"Hello {name}, welcome to innovate")
# else:
#     print("no name was provided")

# allowed = ["Reyan", "Barry", "Bruce", "Arthor", "Hal"]
# name=input("What is your name?: ")

# while name not in allowed:
#     print("Your nmae isnt on the list")
#     print("Try again")
#     name=input("What is your name?: ")

# print("You can enter")

# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")
#     try:
#         print(int(num1) + int(num2))
#     except:
#         print("Please use number only")
#         add_up()
# add_up()

# light = False
# def light_switch():
#     global light
#     if light:
#         print("Whoa! It's bright in here")
#         light = False
#     else:
#         print("Who turned out the lights?")
#         light = True

# light_switch()
# light_switch()
# light_switch()

# even_nums = [2,4,6,8,10] # list can be changed
# # we can insert, remove, append, pop and more to change the properties.
# even_nums.append(12)
# even_nums.insert(0,0)
# print(even_nums)

# odd_nums = (1,3,5,7,9) # this is a tuple, you can not change by methods
# odd_nums.append(11)
# # odd_nums.append(11) - this will not work on a tuple.
# print(odd_nums)

# fav_games = [
#     "Farcry 3",
#     "The Outerworlds",
#     "Starwars Jedi: Fallen order"
# ]

# print(fav_games[0:3:1]) # [0:3:1] - [start:stop:step]

# test = "madam"

# if test == test [::-1]:
#     print(f"Yes {test} is a palindrome")
# else:
#     print("It is not a palindrome")

#------------------------------------------------------------------------------------------------------------------------------------------------#

# num=random.randint(1,50)
# while num%2==0:
#     print("We like even numbers! Another!")
#     num=random.randint(1,50)
# #if the number is odd, the while loop will never ever run
# print("Oh no! An odd number!")
# ######################################################
# while True:
#     num=random.randint(1,50)
#     print(num)
#     if num%2==0:
#         print("We like even numbers! Another!")
#         continue
#     else:
#         print("An odd number!")
#         break
#this while loop will always initialise. It mihght go straight to the else/break - but it will have started

#------------------------------------------------------------------------------------------------------------------------------------------------#

# allowed = ["Reyan", "Barry", "Bruce", "Arthor", "Hal"]
# name=input("What is your name?: ")

# while name not in allowed:
#     print("Your nmae isnt on the list")
#     print("Try again")
#     name=input("What is your name?: ")

# print("You can enter")

# def add_up():
#     num1 = input("What is the first number you'd like to add up? \n")
#     num2 = input("What is the second number you'd like to add up? \n")
#     try:
#         print(int(num1) + int(num2))
#     except:
#         print("Please use number only")
#         add_up()
# add_up()


#------------------------------------------------------------------Activity----------------------------------------------------------------------#


# def user_num():
#     number = input("Choose a number: ")
#     try:
#         print(f"{int(number)} has been changed to an integer.")
#     except:
#         print("Try again please.")
#         user_num()
# user_num()

#----------------------------------------------------------------------#

def answer_num():
    answer = input("Please type in a number: ")

    try:    
        print(int(answer))
        print(type(int(answer)))
    except:
        print("Try again.")
        answer_num()

answer_num()