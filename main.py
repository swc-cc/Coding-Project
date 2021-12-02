

pollResult = []
pollOption = [
    "machine learning", "web development", "graphic/ui design", "blockchain",
    "competitive programming"
]
pollOptionSimplified = ["mach", "web", "graph", "block", "compro"]
newPeople = 0

print(
    "Welcome to the SWC Coding Club Poll! Choose an option to explore in Computer Science! Here are some options:"
)
print(pollOption)
print(
    "Enter your option: 'mach' for machine learning, 'web' for web development, 'graph' for graphic/ui design, 'block' for blockchain and 'compro' for competitive programming."
)
for i in range(0, 6):
    print('Person', (i + 1))
    print("Please Enter your Option Here")
    newChoice = input()
    while newChoice not in pollOptionSimplified:
        print("invalid option, please see our options")
        newChoice = input()
    else:
        pollResult.append(newChoice)

machine_learning = pollResult.count("mach")
web_development = pollResult.count("web")
graphic_or_ui_design = pollResult.count("graph")
blockchain = pollResult.count("block")
competitive_programming = pollResult.count("compro")


def largest(s1, s2, s3, s4, s5):
    if (s1 > s2) and (s1 > s3) and (s1 > s4) and (s1 > s5):
        largest_num = "machine learning"
    elif (s2 > s1) and (s2 > s3) and (s2 > s4) and (s2 > s5):
        largest_num = "web development"
    elif (s3 > s1) and (s3 > s2) and (s3 > s4) and (s3 > s5):
        largest_num = "graphic/ui design"
    elif (s4 > s1) and (s4 > s3) and (s4 > s2) and (s4 > s5):
        largest_num = "blockchain"
    else:
        largest_num = "competitive programming"
    print("The option which get the most votes is: ", largest_num)

print(largest(machine_learning, web_development, graphic_or_ui_design, blockchain, competitive_programming))