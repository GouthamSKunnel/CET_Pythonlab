def factor(a):
    for x in range (1,a+1):
        if a%x == 0:
            print(x)
            
num=int(input("Enter the number "))
factor(num)

        
        
