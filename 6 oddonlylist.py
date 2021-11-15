list1=list(map(int,input("enter list: ").split()))
new_list=[x for x in list1 if x%2 !=0]
print("After removing even values :  ",new_list)
