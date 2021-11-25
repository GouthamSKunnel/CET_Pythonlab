def factorial(a):
    fact=1;
    while(a!=0):
        fact=fact*a
        a-=1
    return fact


num=int(input("Enter the number "))
print(factorial(num))

        
        
