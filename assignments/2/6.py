'''
  CSC101 - Programming Assignment 01 Part 1
  2.6 - Sum the digits in an integer
  Sean Xiao
  May 10th, 2021
  
  Summary
    This program accepts a number from 1-999 and will then calculate and output the sum of all the digits in the number.
'''

number = int(input("Enter a number between 0 and 1000: "))
if number < 0 or number > 999:
    print("The number is not valid.")
else:
    print("Sum of all digits:", \
        (number // 100) % 10 +\
        (number // 10) % 10 +\
        number % 10\
    )
