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
#unique_elements = set()

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

print("\n7. Find the maximum number in the numbers list. Then, for each item in the lists of the odds_evens dictionary,"
      "\n add this maximum number to the item and append the result to the numbers list."
      "\n Try this using dictionary comprehension!")

# Find the maximum number in the numbers list...
max_number = max(numbers)
print("maximum number in list = ", max_number)

# ...for each item in the lists of the odds_evens dictionary add this maximum number to the item...
numbers_max = [n + max_number for n in numbers]

print("numbers: ", numbers)
print("numbers + max: ", numbers_max)

# ...and append the result to the numbers list.
numbers.extend(numbers_max)
print("Extended numbers (unique): ", list(set(numbers)))

new_numbers = {key:[value] for key, value in odds_evens2.items()}
odds_evens3 = {
    key: [x for x in numbers_max if int(x) % 2 == (0 if key == 'even' else 1)]
    for key in ['even', 'odd']
}
print()
print("odds_evens: ", odds_evens)
print("odds_evens2: ", odds_evens2)
print("odds_evens3: ", odds_evens3)


# 8. Take the code you wrote to process #1 – 7 and add error handling with TRY-EXCEPT-FINALLY blocks.
print("\n8. Take the code you wrote to process #1 – 7 and add error handling with TRY-EXCEPT-FINALLY blocks.")

lst1B = ['1', '2', [3]]
lst2B = [('3', 4), '5', 6]
lst1B_2B = lst1B + lst2B
lst3B = []

try:
    for i in lst1B_2B:
        if type(i) == int or type(i) == str:
            lst3B.append(i)
        else:
            for j in i:
                lst3B.append(j)
except AssertionError:
    print("Exception encountered.")
else:
    print(lst3B)
finally:
    print("list3b creation attempted.")

odds_evensB = {'even': [], 'odd': []}

try:
    for item in lst3B:
        # Convert item to int if it's a string representing a number.
        num = int(item) if isinstance(item, str) and item.isdigit() else item

        # Check if the number is even or odd
        if num % 2 == 0:
            odds_evensB['even'].append(item)
        else:
            odds_evensB['odd'].append(item)
except AssertionError:
    print("Exception encountered.")
else:
    print(odds_evensB)
finally:
    print("odds_evensB creation attempted.")

try:
    numbersB = [int(x) for x in lst3B]
    max_numberB = max(numbersB)
    numbers_maxB = [n + max_numberB for n in numbersB]
    numbersB.extend(numbers_maxB)
except AssertionError:
    print("Exception encountered.")
else:
    print("Extended numbers (unique): ", list(set(numbersB)))
finally:
    print("Problem 8 completed.")