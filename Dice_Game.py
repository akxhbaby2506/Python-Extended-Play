import random

dice = random.randint(1,6)
while True:
    print("Warning...!");print("Please enter ur guess from 1 to 6")
    guess = int(input("Enter your guess number: "))
    if guess == dice:
        print("You Finally fot it...!")
        print("the guess number is: ",dice)
        break;
    