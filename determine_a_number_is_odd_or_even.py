# -*- coding: utf-8 -*-
"""Determine a Number is Odd or Even

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13rjSkvggeBKn5EFmpvqUHgJkqtofivk0

Prompts the user to enter a number and prints a message indicating
     whether it is odd or even.
"""

#def is_odd_or_even(number):
number = int(input("Enter a number and the click Enter:  "))

if (number % 2) == 0:
  print("The number {0} is Even".format(number))

else:
  print("The number {0} is Odd".format(number))

#print(f"The number {number} is {is_odd_or_even(number)}.")