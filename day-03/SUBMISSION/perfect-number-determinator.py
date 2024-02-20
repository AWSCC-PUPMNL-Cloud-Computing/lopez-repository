import math

print("PERFECT NUMBER DETERMINATOR FOR ALF")

print("\n")

sumOfDivisors = 0
number = int(input("Please, enter a non-negative integer: "))
if number < 0: 
  while number < 0: 
    print("Invalid.")
    number = int(input("Please, enter a non-negative integer: "))

for i in range(1, number, 1): 
  if i == number: 
    break
  if number % i == 0: 
    sumOfDivisors += i

if sumOfDivisors == number: 
  print("{} is a Perfect Number.".format(number))
else: 
  print("{} is not a Perfect Number.".format(number))