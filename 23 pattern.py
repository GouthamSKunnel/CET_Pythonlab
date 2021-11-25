def pattern(a):
    for i in range(1,a+1):
        
        for j in range(1,i+1):
            print(i*j,end=(' '))
            
        print("\n")
    


num=int(input("Enter the number "))
print(pattern(num))
         
            
