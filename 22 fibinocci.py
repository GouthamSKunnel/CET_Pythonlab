

def fibonacci(n):
	a = 0
	b = 1
	
	if n < 0:
		print("Incorrect input")
		
	
	elif n == 0:
		return 0
	
	elif n == 1:
		return b
	else:
		for i in range(1, n+1):
			c = a + b
			a = b
			b = c
			print(b,"\t")
	    

num=int(input("Enter the number "))
print(fibonacci(num))


