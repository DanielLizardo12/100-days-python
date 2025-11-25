programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
    "item2": "asdasd",
    "item3": "blabla",
}

print(programming_dictionary["item2"])

programming_dictionary["loop"] = "something"

empty_dict = {}

print(programming_dictionary)

programming_dictionary["Bug"] = "new data"

print(programming_dictionary)

for key in programming_dictionary:
    print(key + " : " + programming_dictionary[key])