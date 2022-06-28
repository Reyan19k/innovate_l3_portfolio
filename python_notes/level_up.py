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

# allowed = ["Reyan", "Andy", "Bob", "Carol", "Dean"]
# name=input("What is your name?: ")

# while name not in allowed:
#     print("Your nmae isnt on the list")
#     print("Try again")
#     name=input("What is your name?: ")

# print("You can enter")

def add_up():
    num1 = input("What is the first number you'd like to add up? \n")
    num2 = input("What is the second number you'd like to add up? \n")
    try:
        print(int(num1) + int(num2))
    except:
        print("Please use number only")
add_up()