print("PALINDROME CHECKER FOR ALF")

string = input("Please, enter a word/s to check: ")

if string[::-1] == string: 
  print("'{}' is a palindrome.".format(string))
else: 
  print("'{}' is not a palindrome.".format(string))