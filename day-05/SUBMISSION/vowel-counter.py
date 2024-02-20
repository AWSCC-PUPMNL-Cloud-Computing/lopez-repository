print("VOWEL COUNTER FOR ALF")

numberOfVowels = 0
i = 0
string = input("Please, enter a word/s to check: ")

for i in range(len(string)): 
  if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u" or string[i] == "A" or string[i] == "E" or string[i] == "I" or string[i] == "O" or string[i] == "U":
    numberOfVowels += 1 

print("The number of vowels in {} is: {}".format(string, numberOfVowels))