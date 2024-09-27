'''
/*
 * Program: Promineo Tech Data Engineering (Big Data)
 * Author:  Samuel Ajao
 * Assignment: Week 04 Technical Assignment
 * Create Date: September 26, 2024
 */
'''
from ftplib import print_line

"""
Part 1: Lists
"""

# 1. Create a list called shopping_list that contains at least 5 items you need to buy at the grocery store
shopping_list = ["milk", "eggs", "bacon", "bread", "coffee"]

# 2. Print out the third item in shopping_list.
print("\nProblem 1.2. Third item in list is: " + shopping_list[2])

# 3. Add two more items to the end of shopping_list.
shopping_list.append("orange juice")
shopping_list.append("creamer")

# 4. Remove the first item from shopping_list.
shopping_list.pop(0)

# 5. Print out the final version of shopping_list.
print("\nProblem 1.5. Final shopping list:")
for i in range(len(shopping_list)):
    print(shopping_list[i])

"""
Part 2: Dictionaries
"""

# 1. Create a dictionary called my_info that contains your name, age, and favorite hobby.
my_info = {
    "name": "Bob Burger",
    "age": 40,
    "favorite hobby": "Guitar"
}

# 2. Print out your name from the my_info dictionary.
print("\nProblem 2.2. Print out your name from the my_info dictionary.")
print(my_info["name"])

# 3. Update the value of your favorite hobby in the my_info dictionary.
my_info["favorite hobby"] = "Gaming"

# 4. Add a new key-value pair to the my_info dictionary that contains your favorite food.
my_info["favorite food"] = "Pizza"

# 5. Print out the final version of the my_info dictionary.
print("\nProblem 2.5. Print out the final version of the my_info dictionary.")
print(my_info)

"""
Part 3: Loops
"""
# 1. Create a list called numbers that contains the numbers 1 through 10.
my_list = []
for j in range(10):
    my_list.append(j+1)

#print(my_list)
# 2. Using a for loop, print out each number in the numbers list.
print("\nProblem 3.2 Using a for loop, print out each number in the numbers list.")
for k in range(len(my_list)):
    print(my_list[k])

# 3. Using a while loop, print out each number in the numbers list.
print("\nProblem 3.3. Using a while loop, print out each number in the numbers list.")
m = len(my_list)
n = 0
while n < m:
    print(my_list[n])
    n += 1

# 4. Create a dictionary called squares that contains the squares of the numbers 1 through 5 (e.g. 1: 1, 2: 4, 3: 9, 4: 16, 5: 25).

my_squares = {
    "1": 1,
    "2": 4,
    "3": 9,
    "4": 16,
    "5": 25
}

# 5. Using a for loop, print out each key-value pair in the squares dictionary.
print("\nProblem 3.5. Using a for loop, print out each key-value pair in the squares dictionary.")
for key, value in my_squares.items():
    print(f"{key}: {value}")

"""
Part 4: Conditional Logic
"""
