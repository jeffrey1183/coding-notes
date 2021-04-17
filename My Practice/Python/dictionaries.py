#So dictionaries are yet another data structure in Python which are used in order to map certain values on to other values.
#And they're often used when we want to try and indicate some sort of relationship between a former value and a latter value.
ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30
ages["Alice"] += 1 # equals to ages["Alice"] = ages["Alice"] + 1

print(ages)


# Defne a dictionary
houses = {
    "Harry": "Gryffindor",
    "Draco": "Slytherin"
}

# Print out Harry's house

print(houses["Harry"])

# Adding values to a dictionary:

houses["Hermione"] = "Gryffindor"

# Dictionaries cannot have two items with the same key. Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


