def gcd(a,b):
    if a==0:
        return b
    
    return gcd(b%a,a)

num1,num2=input("enter two numbers ").split()
num1=int(num1)
num2=int(num2)

print (gcd(num1,num2))
