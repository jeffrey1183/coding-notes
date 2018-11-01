#So dictionaries are yet another data structure in Python which are used in order to map certain values on to other values.
#And they're often used when we want to try and indicate some sort of relationship between a former value and a latter value.
ages = {"Alice": 22, "Bob": 27}
ages["Charlie"] = 30
ages["Alice"] += 1 # equals to ages["Alice"] = ages["Alice"] + 1

print(ages)
