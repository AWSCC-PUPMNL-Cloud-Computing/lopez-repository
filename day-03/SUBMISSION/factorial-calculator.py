import math

print("FACTORIAL CALCULATOR FOR ALF")

print("\n")

number = int(input("Please, enter a non-negative integer: "))
if number < 0: 
  while number < 0: 
    print("Invalid.")
    number = int(input("Please, enter a non-negative integer: "))
answer = math.factorial(number)

print("The factorial of {} is: {}".format(number, answer))