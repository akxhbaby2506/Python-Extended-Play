b = float(input("Enter the bill amount: "))
p = float(input("Enter the amount paid: "))

if p == b:
    print("No change has to be given.")
    
elif p < b :
    print("Ask the customer to stfu and give an amount of,",b-p)
    
elif p > b :
    
    x = p-b
    
    c2000 = x//2000
    x = x - (c2000*2000)
    
    c500 = x//500
    x = x - (c500*500)
    
    c200 = x//200
    x = x - (c200*200)
    
    c100 = x//100
    x = x - (c100*100)
    
    c50 = x//50
    x = x - (c50*50)
    
    c20 = x//20
    x = x - (c20*20)
    
    c10 = x//10
    x = x - (c10*10)
    
    c5 = x//5
    x = x - (c5*5)
    
    c2 = x//2
    x = x - (c2*2)
    
    c1 = x//1
    x = x - (c1*1)
    
    print("Change for Rs.2000 note is: ",c2000)
    print("Change for Rs.500 note is: ",c500)
    print("Change for Rs.200 note is: ",c200)
    print("Change for Rs.100 note is: ",c100)
    print("Change for Rs.50 note is: ",c50)
    print("Change for Rs.20 note is: ",c20)
    print("Change for Rs.10 note is: ",c10)
    print("Change for Rs.5 note is: ",c5)
    print("Change for Rs.2 note is: ",c2)
    print("Change for Rs.1 note is: ",c1)
