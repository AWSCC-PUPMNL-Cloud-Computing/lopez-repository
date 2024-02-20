print("BMI CALCULATOR FOR ALF")

print("\n")

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

print("\n")

BMI = weight/(height**2)
if BMI > 30.0: 
  nutriStatus = "obesity"
elif BMI < 30.0 and BMI > 24.9: 
  nutriStatus =  "overweight"
elif BMI < 25.0 and BMI > 18.4:
  nutriStatus = "normal weight"
else:
  nutriStatus = "underweight"    
 
print("HEIGHT: %.2f - WEIGHT: %.2f" % (height, weight))
print("BMI: %.2f - NUTRITIONAL STATUS: %s" % (BMI, nutriStatus))