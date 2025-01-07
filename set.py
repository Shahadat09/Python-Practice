my_set = {1, 2, 3, 4, 6, 8, "atik"}
print(my_set)
print(type(my_set))
print("*" * 50)

# Adding an element to the set
my_set.add(9)
print(my_set)
print("*" * 50)

# Removing an element from the set
my_set.discard(2)
print(my_set)
print("*" * 50)

# Pop an element from the set (removes and returns an arbitrary element)
print(my_set)
popped_element = my_set.pop()
print(popped_element)
print("*" * 50)

# Iterating through the set
for i in my_set:
    print(i)
print("*" * 50)

# Checking the existence of a value in the set
print(my_set)
print(1 in my_set)  # Checks if 1 exists in the set
print(3 in my_set)  # Checks if 3 exists in the set
print("*" * 50)

my_set1 = {1, 2, 3, 4, 5, 7}
my_set2 = {1, 2, 3, 4, 5, 7, 8, 9, 6}

# Union of two sets: Combines elements from both sets and removes duplicates
print("Union value", my_set1 | my_set)
print("*" * 50)

# Intersection of two sets: Gives common elements present in both sets
print("Intersection", my_set1 & my_set2)
print("*" * 50)

# Difference between two sets: Elements present in my_set2 but not in my_set1
print("Difference", my_set2 - my_set1)
print("*" * 50)


# Symmetric Difference: Elements that are in either of the sets but not in both
print("Symmetric Difference", my_set1 ^ my_set2)
print("*" * 50)

#to clear all values

print(my_set1)
my_set1.clear()
print(my_set1)