# First name: Samuel

# Last name: Ajao

# Cohort: Data Engineering - Eastern

# Submission date: October 5, 2024

# Assignment: Comprehensions

print("\n1. lst1 = ['1', '2', [3]]")
lst1 = ['1', '2', [3]]
print(lst1)

print("\n2. lst2 = [('3', 4), '5', 6]")
lst2 = [('3', 4), '5', 6]
print(lst2)

print("\n3. Join lst1 and lst2 so only unique string or integer values remain in a new list, lst3.(i.e.,"
      " ['1', '2', 3, '3', 4, 5, 6])")
lst1p2 = lst1 + lst2
print(lst1p2)
lst3 = []
unique_elements = set()

for i in lst1p2:
    if type(i) == int or type(i) == str:
        lst3.append(i)
    else:
        for j in i:
            lst3.append(j)
print("\nResult: ", lst3)

print("\n4. Create an empty dictionary called odds_evens. Next, iterate through lst3. If a number (regardless of datatype)"
      " \nis even, add the value to a list that will be stored as a value for the key even in the dictionary, odds_evens."
      " \nDo the same for the odds numbers. When you print the odds_evens dictionary the output should look like this:"
      " \n{'evens': ['2', 4, 6], 'odds': ['1', '3', 3, '5']}")

odds_evens = {'even': [], 'odd': []}

for item in lst3:
    # Convert item to int if it's a string representing a number.
    num = int(item) if isinstance(item, str) and item.isdigit() else item

    # Check if the number is even or odd
    if num % 2 == 0:
        odds_evens['even'].append(item)
    else:
        odds_evens['odd'].append(item)
print(odds_evens)

print("\n5. Next, loop through lst3 and evaluate each item using a list comprehension. if it's not an integer,"
      " \nconvert it to an integer. The resulting list should be called, numbers.")

#This uses a ternary conditional expression to dynamically adjust the condition based on the current key.
odds_evens2 = {
    key: [x for x in lst3 if int(x) % 2 == (0 if key == 'even' else 1)]
    for key in ['even', 'odd']
}
print(odds_evens2)

print("\n6. Then, iterate through the values in the odds_evens dictionary. For each number, if it's a string, "
      "\nconvert it to an int, otherwise ignore.")
print("list3 = ", lst3)
numbers = [int(x) for x in lst3]
print("numbers = ", numbers)
