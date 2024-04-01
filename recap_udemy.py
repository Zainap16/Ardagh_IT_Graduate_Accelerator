programming_dictionary = {
    "Cat" : "feline",
    "Dog" : "canine"
}

# view from dict
print(programming_dictionary["Cat"])

# add dict
programming_dictionary["Lion"] = "big feline"
print(programming_dictionary["Lion"])
print("\n\n")
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])