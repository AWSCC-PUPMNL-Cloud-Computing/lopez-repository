import csv
import json

with open('example1.csv', 'r') as file: 
  csvRead = csv.reader(file)

  for line in csvRead: 
    print(line[0])

file.close()

with open('example2.json', 'r') as file1: 
  jsonRead = json.load(file1)

  for line in jsonRead: 
    print(line)