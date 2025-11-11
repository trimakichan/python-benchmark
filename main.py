# Beneath each comment write the code and print out the result to check it works

'''LISTS'''
print("=================Lists=================")
# Create a list and assign it to a variable
my_list = ["May", "Joy", "Anna", "Josh"]
print(my_list)

# Find the length of the list
print(len(my_list))

# Append an item to the list
my_list.append("Makiko")
print(my_list)

# Find the value of an item in the list a specific index
print(my_list[2])

# Set the value of an item at a specific index REVIEW
my_list[2:2] = ["Maddie", "Sara"]
my_list.insert(1, "kiki")

print(my_list)

# Check whether an item is in the list
result = "Joy" in my_list
print(result)

# Sort the list
my_list.sort()
print(my_list)

# Iterate over the list using range, printing out each element and the index
for index in range(len(my_list)):
    print(index, my_list[index])

# Iterate over the list without using range, printing out each element
for name in my_list:
    print(name)

'''TUPLES'''
print("=================Tuples=================")

# Create a tuple and assign it to a variable
my_tuple = (1,2,3,4)
my_empty_tuple = ()
print(type(my_tuple), type(my_empty_tuple))

# Find the length of the tuple
print(len(my_tuple))

# Find the value of an item in the tuple a specific index
print(my_tuple[1])

# Check whether an item is in the tuple
print(7 in my_tuple)

# Iterate over the tuple using range, printing out each element and the index
for index in range(len(my_tuple)):
    print(index, my_tuple[index])

# Iterate over the tuple without using range, printing out each element
for num in my_tuple:
    print(num)

'''STRINGS'''
print("=================Strings=================")

# Create a string and assign it to a variable
string1 = "hello"
print(string1)

# Find the length of the string
print(len(string1))

# Find the value of an character in the string a specific index
print(string1[1])

# Check whether an item is in the string
print("h" in string1)

# Concatenate (add) two strings together
print("Hello, " + "there")

# Create an f-string
print(f"This is f-string.")

# Split a string using .split !!!!!Check!!!!!
string2 = "apple banana orange"
split_list = string2.split()
print(split_list)

# Join a list of strings using .join !!!!!Check!!!!!
print(" ".join(split_list))

# Iterate over the string using range, printing out each character and the index
for i in range(len(string1)):
    print(string1[i])

# Iterate over the string without using range, printing out each character
for char in string1:
    print(char)

'''DICTIONARIES'''
print("=================Dictionaries=================")

# Create a dictionary and assign it to a variable
fruits = {"apple": 1, "orange": 2}
print(fruits)

# Find the length of the fruits 
print(len(fruits))

# Add a new key/value pair !!!!!Check!!!!!
fruits["banana"] = 3
print(fruits)

# Replace value for a given key
fruits["apple"] = 2
print(fruits)

# Check whether a key is in the fruits !!!!!Check!!!!!!
result = "kiwi" in fruits
print(result)

# Iterate over keys, printing each key
for fruit in fruits:
    print(fruit)

# Iterate over over key/value pairs using .items(), printing each key and value
for fruit, count in fruits.items():
    print(fruit, count)

'''SETS'''
print("=================Sets=================")
# Create a set and assign it to a variable
my_set = set()
my_set1 = {1, 2, 3}
print(type(my_set))
print(my_set1)

# Find the length of the set
print(len(my_set1))

# Add a new element !!!!!Check!!!!!!
my_set1.add(4)
my_set1.add(1)
print(my_set1)

# Remove an element
my_set1.remove(2)
print(my_set1)

# Check whether a element is in the set
print(2 in my_set1)

# Iterate over elements, printing each one out
for num in my_set1:
    print(num)

'''NUMBERS'''

# Add / subtract / multiply 2 numbers
print("=================Numbers=================")
addition = 1 + 1
print(addition)

subtraction = 5-1
print(subtraction)

multiplication = 2 * 4
print(multiplication)

# Divide two numbers using normal (float) division
division = 5 / 2
print(division)

# Divide two numbers using integer division
integer_division = 5 // 2
print(integer_division)

# Find the modulo (remainder) of two numbers
modulo = 3 % 2
print(modulo)

# Check whether a number is even/odd
is_even = 5 % 2 == 0
print(is_even) 

# Round a float down to an int
print(int(-3.6 // 1))
print(int(-3.7))


'''FUNCTIONS'''
print("=================Functions=================")

# Write a function that takes no arguments and call it

def say_hello():
    print("Hi!")

say_hello()

# Write a function that takes one or more arguments and call it
def say_hello(name):
    print(f"Hi, {name}")

say_hello("Joy")

# Write a function that returns a value. Call the function and store the return value in a variable
def say_hello():
    return "Hello, there!"

result = say_hello()
print(result)

'''LOOPS'''
print("=================Loops=================")

# Write a while loop
counter_variable = 0

while counter_variable < 2:
    print(counter_variable)
    counter_variable += 1

# Write a for loop that loops a set number of times (e.g. 10 times)
counter_variable = 0

while counter_variable < 10:
    print(counter_variable)
    counter_variable += 1

'''CONDITIONALS'''
print("=================CONDITIONALS=================")

# Write an if/elif/else statement
age = 89
if age < 1:
    print("baby")
elif age < 13:
    print("from toddler to pre-teen")
else:
    print("you are getting old.")

# Write conditionals for the following operators:
# ==
print(2 == "2")
# !=
print("tomato" != "tomato")
# <
print( 2 < 4)
# >
print(4 > 1)
# <=
print(3 <= 3)
# >=
print(5 >= 10)

'''NESTED DATA'''
print("=================NESTED DATA=================")
# Write a nested list (a list of lists) and assign it to a variable
nested_list = [["apple", "orange"], ["tomato", "carrot"]]

# Print an item at a specific position in the data structure (e.g. the item at a given row and column). HINT: row comes first, column comes second
print(nested_list[1][1])

# Iterate through the nested data structure using range
for i in range(len(nested_list)):
    for j in range(len(nested_list[i])):
        print(nested_list[i][j])

# Iterate through the nested data structure without using range 
for items in nested_list:
    for item in items:
        print(item)

'''REMINDER'''


# You're doing great and you got this!


# Use lambda functions with max and min to find the longest and shortest words in a list
words = ["apple", "banana", "kiwi", "strawberry", "fig"]

nums = [-10, -3, 2, 8]
# Find the number with the largest absolute value (use abs)

cities = {"Tokyo": 37, "Delhi": 31, "Shanghai": 27, "New York": 19}
# Find the city with the largest population

employees = [
    {"name": "Tom", "hours": 40},
    {"name": "Anna", "hours": 52},
    {"name": "John", "hours": 45}
]
# Find the employee who worked the most hours
inventory = [
    {"name": "apple", "price": 2, "quantity": 50},
    {"name": "banana", "price": 1, "quantity": 100},
    {"name": "pear", "price": 3, "quantity": 30}
]
# Find the product with the highest total value
