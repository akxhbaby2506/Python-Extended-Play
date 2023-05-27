import random

a = int(input("Enter the starting point: "))
b = int(input("Enter the ending point: "))
num = random.randint(a,b)
print(num)
while True:
    print("You have to input your guess from ",a, " to ",b)
    guess = int(input("Enter your guess number: "))
    if guess == num:
        print("Congratulations...! It's a Perfect guess")
        print("the guess number is: ",num)        
        break
    elif guess > num:
        print("Lower Number please...!")
    elif guess < num:
        print("Higher Number please...!")
