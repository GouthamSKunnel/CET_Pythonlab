num = int(input("Enter the number "))

# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
