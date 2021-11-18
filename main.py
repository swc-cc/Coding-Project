pollResult = {}
pollOption = ["machine learning", "web dev",  "graphic/ui design", "blockchain", "competitive programming"]
newPeople = 0

print("Welcome to the SWC Coding Club Poll! Choose an option to explore in Computer Science! Here are some options:")
print(pollOption)
for i in range(0, 41):
  print('Person', (i + 1))
  print("Please put your name first, then press 'Enter' and put your Option")
  newName = input()
  newChoice = input()
  while newChoice not in pollOption:
    print("invalid option, please see our options")
    newChoice = input()
  else:
    pollResult[newName] = newChoice

print(pollResult)