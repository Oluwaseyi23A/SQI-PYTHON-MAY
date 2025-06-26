# favorite_colour = input('enter your favorite colour: ')
# print(f'{favorite_colour} is awesome!')

# first_name = input('What is your first name? ')
# last_name = input('What is your last name? ')
# fullname = first_name + ' ' + last_name
# print(f'Good Morning {fullname}')

# birth_year = int(input('enter your year of birth '))
# current_year = 2025
# age = current_year - birth_year
# print(f'You are {age} years old')
 
from datetime import datetime


# Assignment
# # Write a program that asks the user for their name and then greets them with their name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# name = input('Please enter your name: ')
# print(f'Hello, {name}!')

# # Ask the user for their birth year and calculate their age. Print the user's age in the 
# format “You are {age} years old.”.

# birth_year = input("Please enter your birth year: ")
# age = datetime.now().year - int(birth_year)
# print(f"You are {age} years old.")

# Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.

# favourite_colour = input('What is your favourite colour? ')
# print(f'Your favourite colour is {favourite_colour}!')

# Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.

# text = input("Please enter some text: ")   ***
# is_palindrome = True
# print(f"It is {is_palindrome} that is a girl.")

# # Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.Bonus point if you can hide the password input from displaying on the screen as clear text.

# password = input("Please enter a password: ")
# is_valid = 8 <= len(password) <= 30
# print(f"It is {is_valid} that the password fulfils the criteria.")

# Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.

weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters: "))
bmi = round(weight / (height ** 2), 2)
print(f"Your BMI is {bmi}.")





