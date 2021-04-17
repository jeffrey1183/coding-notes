#A set is just a collection of items where no item shows up twiceself.
#And in particular, a set doesn't have any particular order to it.
#So the only thing we care about is a particular value in the set, or is a particular value not in the set?
s = set()

#where set is just a function that creates an empty set for me.
s.add(1)

# I've added the number 1 to the set.

s.add(3)
s.add(5)
s.add(3)
print(s)

# What I get is {1,3,5}
# Despite adding 3 to the set twice, each item can only appear once in a set.

# Remove 5 from the set
s.remove(5)

print(s)

# Find the size of the set:
print(f"The set has {len(s)} elements")