side=int(input("Enter the side of the square "))
square = lambda a: a * a
print("Area of square ",square(side))

leng=int(input("Enter the length of the rectangle "))
br=int(input("Enter the breadth of the rectangle "))
rectangle = lambda a, b : a * b
print("Area of rectangle ",rectangle(leng, br))

height=int(input("Enter the height of the triangle "))
breadth=int(input("Enter the breadth of the triangle "))
triangle = lambda a, b : (a * b)/2
print("Area of triangle ",triangle(height, breadth))
