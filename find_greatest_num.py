num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

print()

print("Methord-1: Using In-Built Function")
greatest = max(num1,num2,num3,num4)
print("The greatest value of the numbers is: ",greatest)

print()

print("Methord-2: Using Fighting methord")
if num1>num2:
    x = num1
else:
    x = num2
    
if num3>num4:
    y = num3
else:
    y = num4
    
if x>y:
    print(x," is the greatest value of the numbers")
else:
    print(y," is the greatest value of the numbers")
    
    