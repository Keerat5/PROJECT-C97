import random
n = random.randint(1,9)
chances=0
while chances<5:
    guess=int(input("Enter your guess"))
    if guess==n:
        print("Congo!!!! You guessed the correct number")
        break
    elif guess<n:
        print("Your guess is too low...")
    else:
        print("Your number is too high...")
    chances+=1
if chances==5:
    print("You lost :(")    



    

