import random
a = input("Enter Rock/Paper/Scissors: " ).lower()
moves = ["rock", "paper", "scissors"]
b = random.choice(moves)
print ("Computer choose:",b)

if (a == b):
    print("its a Draw")
elif(a == "rock" and b =='paper'):
    print("comp","Wins..!")
elif(a == "rock" and b =='scissors'):
    print("Player",'Wins..!')
elif(a == 'paper' and b == "rock"):
    print("Player","Wins..!")
elif(a == 'paper' and b == "scissors"):
    print("Comp",'Wins..!')
elif(a == 'scissors' and b == "rock"):
    print("Comp",'Wins..!')
elif(a == 'scissors' and b == "paper"):
    print("Player",'Wins..!')
else:
    print('Please input proper arguments')
    