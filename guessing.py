import random
rn = random.randint(1, 100)
guesscheck = False
while guesscheck == False:
    guess = int(input("Guess the number: "))
    if guess > rn:
        print("Too high!")
    if guess < rn:
        print("Too low!")
    if guess == rn:
        print("You got it!")
        guesscheck = True