import math

print("CYLINDER VOLUME CALCULATOR FOR ALF")

print("\n")

a = float(input("Please, enter the length of side A: "))
b = float(input("Please, enter the length of side B: "))
csqr = math.pow(a, 2) + math.pow(b, 2)
c = float(math.sqrt(csqr))

print("The hypotenuse of the right-angled triangle is: %.2f" % (c))