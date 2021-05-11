'''
  CSC101 - Programming Assignment 01 Part 1
  2.10 - Physics: find runway length
  Sean Xiao
  May 10th, 2021
  
  Summary
    This program calculates the minimum runway length for a airplane to take off with it's take off speed and acceleration.
'''
speed = float(input("Enter meters per second (take off speed): "))
acceleration = float(input("Enter acceleration: "))

print("The minimum runway length for this airplane is:", 
      round(speed ** 2 / (2 * acceleration), 5)
)
