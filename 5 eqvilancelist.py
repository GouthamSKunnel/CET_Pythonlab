str1=input("Enter first list ")
str2=input("Enter second list ")

list1=list(map(int,str1.split()))
list2=list(map(int,str2.split()))

#list1=list(map(int,input("enter first list: ").split()))
#list2=list(map(int,input("enter second list: ").split()))

if len(list1)==len(list2):
    print("both lists have same length ")
else:
    print("they dont have the same length ")

if sum(list1)==sum(list2):
    print("Both lists have same sum ")
else:
    print("They dont have the same sum")

if not set(list1)==set(list2) :
    print("list values are not the same ")
else:
    print("They have the same elements ")
