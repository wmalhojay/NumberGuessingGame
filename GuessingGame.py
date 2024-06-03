import random

print("Guessing Game Python")
level = input("Choose easy/medium/hard")

def desC(rand, loop):
    print(rand)
    for i in range(loop):
        temp = int(input("Guess --> "))
        if temp == rand:
            print("Guessed it right")
            break
        elif abs(temp - rand) <= 5:
            if temp>rand:
                print("little low")
            else:
                print("little high")
        else:
            if temp>rand:
                print("too low")
            else:
                print("too high")

if level == "easy":
    print("I'm thinking of a number between 1 and 100 \nYou have 10 attempts to Guess")
    desC(random.randint(1, 100), 10)
    
elif level == "medium":
    print("I'm thinking of a number between 1 and 50 \nYou have 5 attempts to Guess")
    desC(random.randint(1, 50), 5)
else:
    print("I'm thinking of a number between 1 and 20 \nYou have 3 attempts to Guess")
    desC(random.randint(1, 20), 3)
