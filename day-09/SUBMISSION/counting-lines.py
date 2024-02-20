with open('story.txt', 'r') as file: 
  read = file.readlines()
  totalLines = len(read)
  print(totalLines)

file.close()