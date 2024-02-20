import math

print("CYLINDER VOLUME CALCULATOR FOR ALF")

print("\n")

r = float(input("Please, enter the radius of the cylinder: "))
h = float(input("Please, enter the height of the cylinder: "))
volume = math.pow(r, 2) * h * math.pi

print("The volume of the cylinder is: %.2f" % (volume))