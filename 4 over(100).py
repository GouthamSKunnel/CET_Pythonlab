values=input("enter integers values: ").split()
new_list=[]
for value in values:
    if int(value) > 100:
        new_list.append("over")
    else:
        new_list.append(int(value))
            
print(new_list)

#integers =[int(x) if int (x)<= 100 else"over" for x in values]
#print(integers)
