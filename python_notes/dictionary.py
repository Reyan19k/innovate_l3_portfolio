#---Example---#

# my_cat = {
#     "name": "Salem",
#     "colour": "White",
#     "mood": "Sassy"
# }

# my_dog = {
#     "name": "Bravo",
#     "colour": "Black",
#     "mood": "Happy"
# }

# my_dog["mood"] = "hungry"

# print(my_dog["name"])
# print(f'My dog {my_dog["name"]} is very {my_dog["mood"]} today')

# print(my_dog.keys()) # shows all the keys

# dog_keys = my_dog.keys()
# my_dog["age"]=2
# print(dog_keys)

# print(my_dog.values())
# print(my_dog.items())
# print(my_dog.get("mood"))

# print(my_dog.get("legs","This key doesn't exist"))


# my_list = ["hello","hello","goodbye"]

# y = my_list.count("hello")

# my_list.appand("hello")

# print(my_dog.keys()) # a bit messy
# print(list(my_dog.keys())) # a little bit cleaner

# for i in my_dog.keys(): # alot more cleaner
#     print(i)

# my_dog.update({"legs":"4"}) # a new key and value
# my_dog.update({"colour":"brown"}) # change an existing key's value
# # my_dog.pop("mood") # this will remove a key
# print(my_dog)

#------------------------------------------------------------------Activity 2----------------------------------------------------------------------#

dif_countries = {
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid",
    "Italy": "Rome"
}

dif_countries.update({"USA":"Washington DC"})
dif_countries.update({"Australia":"Canberra"})

dif_countries.update({"UK":"English"})
dif_countries.update({"France":"French"})
dif_countries.update({"Germany":"German"})
dif_countries.update({"Spain":"Spanish"})
dif_countries.update({"Italy":"Italian"})
dif_countries.update({"USA":"English"})
dif_countries.update({"Australia":"English"})
print(dif_countries)