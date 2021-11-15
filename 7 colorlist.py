color_list1=input("Enter the colors ").split()
color_list2=input("Enter the 2nd list ").split()

for item in color_list1:
    if item not in color_list2:
        print (item)