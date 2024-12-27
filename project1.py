import random
'''
1 for snake 
-1 for water 
0 for gun

'''

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w": -1, "g": 0}
reserveDict = {1:"Snake", -1: "Water", 0: "Gun"}

you = youDict[youstr]

print(f"You Chose {reserveDict[you]}\n computer chose {reserveDict[computer]}")
if you == computer:
    print("It's a Draw!")
else:
    if (you == -1 and computer == 1):
        print("You Win!")
    elif (you == -1 and computer == 0):
        print("You Lose!")
    elif (you == 1 and computer == -1):
        print("You Lose!")
    elif (you == 0 and computer == 1):
        print("You Win!")
    elif (you == 0 and computer == -1):
        print("You Win!")
    elif (you == 1 and computer == 0):
        print("You Lose!")
    else:
        print("Invalid Input")



