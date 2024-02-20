print("SIMPLE CALCULATOR FOR ALF")
print("\n")

firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ") 


if operator == '+': 
  answer = firstNumber + secondNumber
elif operator == '-': 
  answer = firstNumber - secondNumber
elif operator == 'x': 
  answer = firstNumber * secondNumber
elif operator == '/': 
  answer = firstNumber/secondNumber

print("The result of %.1f %s %.1f is %.1f" % (firstNumber, operator, secondNumber, answer))
