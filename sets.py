# fruits = {"apple", "banana", "mango"} This is a set

# s = set() To create an empty set we cannot use s = {} as it will create a dictionary

# nums = {1, 2, 3, 1, 2, 3}
# print(nums)  
# Output:  {1, 2, 3}

# for item in s:
#     print(item) 
# since we cannot access the elements of a set directly we use the above method to get the elemets of a set. 

# fruits = {"apple", "banana"}
# fruits.add("mango")
# print(fruits) 
# Adding an element inside our set using add() method

# fruits = {"apple", "banana"}
# fruits.update(["mango" , "grapes"])
# print(fruits) 
# Adding an element inside our set using update() method

# fruits = {"apple", "banana"}
# fruits.remove("banana")
# removes the specified element from the set. If the element is not present, it raises a KeyError.

# fruits = {"apple", "banana"}
# fruits.discard("banana")
# removes the specified element from the set. If the element is not present, it does nothing.

# fruits = {"apple", "banana"}
# fruits.pop()
# removes a random element from the set.

# # fruits = {"apple", "banana"}
# fruits.clear()
# print(fruits)  # Output: set() as it removes all the elements from the set.

# # a = {1, 2, 3}
# # b = a.copy()
# # print(b) 
# This is used to create a shallow copy of the set

# ----------- Some common operations on sets ---------------

# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.intersection(b))  Output: {2, 3} as it returns the common elements in both sets

# print(a.union(b)) Output: {1, 2, 3, 4} as it returns all the elements in both sets

# print(a.difference(b)) Output: {1} as it returns the elements in set a that are not in set b

# print(a.symmetric_difference(b)) Output: {1, 4} as it returns the elements in set a that are not in set b and the elements in set b that are not in set a.

# print(a.issubset(b))  Output: False as it returns True if all elements of set a are present in set b

# print(a.issuperset(b)) Output: False as it returns True if all elements of set b are present in set a

# print(a.isdisjoint(b)) Output: False as it returns True if both sets have no elements in common


# a = {1, 2, 3}
# b = {2, 3, 4}
# a.intersection_update(b)  # Updates set a with the intersection of sets a and b
# print(a)  # Output: {2, 3} as it updates set a with the common elements in both sets

# a = {1, 2, 3}
# b = {2, 3, 4}
# a.difference_update(b)  # Updates set a with the difference of sets a and b
# print(a)  # Output: {1} as it updates set a with the elements in set a that are not in set b

# a = {1, 2, 3}
# b = {2, 3, 4}
# a.symmetric_difference_update(b)  # Updates set a with the symmetric difference of sets a and b
# print(a)  # Output: {1, 4} as it updates set a with the elements in set a that are not in set b and the elements in set b that are not in set a.


