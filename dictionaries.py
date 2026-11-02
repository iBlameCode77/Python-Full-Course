# word = {
#     "python": "A programming language",
#     "html": "Markup language"
# }   
# This is a dictionary in python. It is a collection of key-value pairs. Each key is unique and maps to a value.

# student = dict(
#     name="Yash",
#     age=17,
#     city="Indore"
# )
# This is another way to create a dictionary in python using the dict() constructor.

# data = {}
# This is an empty dictionary. We can add key-value pairs to it later.

# word = {
#     "python": "A programming language",
#     "html": "Markup language"
# }   
# print(word["python"])  # Output: A programming language as it returns the value of the key "python" 

#print(word["JS"])  # Output: It will return error as the key "JS" is not present in the dictionary.

#print(word.get("JS"))  # Output: None as the key "JS" is not present in the dictionary.

# for key, value in student.items():
#     print(key, value)
# This is used to iterate over the key-value pairs of the dictionary.

# student = {
#     "name": "Yash",
#     "age": 17
# }

# print(student.keys())
# Output: dict_keys(['name', 'age']) as it returns the keys of the dictionary.

# print(student.values())
# Output: dict_values(['Yash', 17]) as it returns the values of the dictionary.

# print(student.items())
# Output: dict_items([('name', 'Yash'), ('age', 17)]) as it returns the key-value pairs of the dictionary.  

# student = {
#     "name": "Yash"
# }
# student.update({"age": 17})
# print(student)
# Output: {'name': 'Yash', 'age': 17} as it adds the key-value pair to the dictionary.  

# user = {"name": "Alice", "age": 30, "city": "New York"}

# # 1. Pop an existing key
# age = user.pop("age")
# print(age)   # Output: 30
# print(user)  # Output: {'name': 'Alice', 'city': 'New York'}

# # 2. Pop a non-existing key with a default value
# phone = user.pop("phone", "Not Provided")
# print(phone) # Output: Not Provided

# # Order of insertion: name, age, city
# user = {"name": "Alice", "age": 30, "city": "New York"}

# # Removes the last item ("city": "New York")
# removed_item = user.popitem()

# print(removed_item) # Output: ('city', 'New York')
# print(user)         # Output: {'name': 'Alice', 'age': 30}

# user.clear()
# print(user)  # Output: {} as it removes all the key-value pairs from the dictionary.

# new_dict = user.copy()
# print(new_dict)  # Output: {} as it creates a shallow copy of the dictionary.

# student = {
#     "name": "Yash"
# }
# student.setdefault("age", 17)
# print(student)
# Output: {'name': 'Yash', 'age': 17} as it adds the key-value pair to the dictionary if the key is not present. If the key is present, it does nothing.

# keys = ["name", "age", "city"]
# data = dict.fromkeys(keys)
# print(data)
# Output: {'name': None, 'age': None, 'city': None} as it creates a new dictionary with the specified keys and sets their values to None.

# keys = ["name", "job", "city"]
# values = ["Alice", "Engineer", "New York"]
# Combine them into a dictionary
# my_dict = dict(zip(keys, values))
# print(my_dict)
# Output: {'name': 'Alice', 'job': 'Engineer', 'city': 'New York'}

# keys = ["name", "job", "city"]
# values = ["Alice", "Engineer", "New York"]
# Step 1: Create an empty dictionary
# my_dict = {}
# Step 2: Loop through the indices of the lists
# for i in range(len(keys)):
#     my_dict[keys[i]] = values[i]
# print(my_dict)
# # Output: {'name': 'Alice', 'job': 'Engineer', 'city': 'New York'} without using zip function.

