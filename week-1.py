'''
/*
 * Program: Promineo Tech Data Engineering (Big Data)
 * Author:  Samuel Ajao
 * Assignment: Week 03 Technical Assignment
 * Create Date: September 17, 2024
 */
'''

# 1. Write a program that declares a variable and assigns a string to it, then prints the variable.
text1 = "This is a string."
print(text1)

# 2. Write a program that declares two variables and concatenates them into a single string, then prints the result.
text2A = "This is two"
text2B = " strings concatenated."
text2C = text2A + text2B
print(text2C)

# 3. Write a program that declares a variable and prints the length of the string assigned to the variable.
text3 = "This is a question 3 text"
print(len(text3))

# 4. Write a program that declares a variable and prints the first letter of the string assigned to the variable.
text4 = "This is text for question 4"
print(text4[0])

# 5. Write a program that declares a variable and prints the last letter of the string assigned to the variable.
text5 = "This is text for question 5"
print(text5[len(text5)-1])

# 6. Write a program that declares a variable and prints a slice of the string assigned to the variable, from the 2nd to the 5th character.
text6 = "This is the text for question 6"
print(text6[1:4])

# 7. Write a program that declares a variable and prints a slice of the string assigned to the variable, from the 5th character to the end.
text7 = 'This is the text for question 7'
print(text7[4:])

# 8. Write a program that declares a variable and prints a slice of the string assigned to the variable, from the 2nd to the 5th character in reverse order.
text8 = "This is the text for question 8"
print(text8[1:4][::-1])

# 9. Write a program that declares a variable and prints a slice of the string assigned to the variable, every other character.
text9 = "This is the text for question 9"
print(text9[1::2])

# 10. Write a program that declares a variable and prints a slice of the string assigned to the variable, skipping the first two characters.
text10 = "This is the text for question 10"
print(text10[2:])

# 11. Write a program that declares a variable and prints a slice of the string assigned to the variable, skipping the last two characters.
text11 = "This is the text for question 11."
lenText11 = len(text11)
print(text11[0:lenText11 - 2])

# 12.  Write a program that declares a variable and prints a slice of the string assigned to the variable, skipping the first and last two characters.
text12 = "This is the text for question 12."
lenText12 = len(text12)
print(text12[1:lenText12 -2])

# 13. Write a program that declares a variable and converts the string assigned to the variable to all uppercase letters.
text13 = "this is the text for question 13."
print(text13.upper())

# 14. Write a program that declares a variable and converts the string assigned to the variable to all lowercase letters.
text14 = "THIS IS THE TEXT FOR QUESTION 14."
print(text14.lower())

#15. Write a program that declares a variable and replaces a portion of the string assigned to the variable with a new string.
text15 = "This is the text for problem 15."
textAppended = " appended "
text15 = text15[0:11] + textAppended[0:] + text15[12:]
print(text15)