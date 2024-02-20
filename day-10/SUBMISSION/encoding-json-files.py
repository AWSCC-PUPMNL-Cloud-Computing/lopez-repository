import json 

name = input("Enter your name: ")
age = input("Enter your age: ")
faveFood = input("Enter your favorite food: ")

data = {
  "Name" : name,
  "Age" : age,
  "Favorite Food" : faveFood 
}

content = json.dumps(data, indent = 2)

with open('output.json', 'w') as file: 
  file.write(content)

file.close()