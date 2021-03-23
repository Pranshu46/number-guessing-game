import random

number = random.randint(1,9)



chance = 0

while chance < 5:   
    guess = int(input("Enter the number"))


    if guess == number:
        print ("congratulations you won")

    elif guess < number :
        print ("your guess was too low", guess)

    else :
        print("your guess was too high", guess)
    chance = chance+1

if not chance < 5:
    print("you lose. the number is",number)
   