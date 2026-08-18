#nested if questions
s1 = float(input("Enter the first side of a triangle: "))
s2 = float(input("Enter the second side of a triangle: "))
s3 = float(input("Enter the third side of a triangle: "))
lst = [s1,s2,s3]
lst.sort()
a = lst[0]
b = lst[1]
c = lst[2]
if (a + b > c):
    print("it is a valid triangle")
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isoceles")
    else:
        print("Scalar")
else:
    print("not a valid triangle")

#marks and grade calculator
marks = int(input("Enter marks from (0-100): "))
if  90<=marks<=100:
    print("A grade")
elif  80<=marks<90:
    print("B grade")
elif  70<=marks<80:
    print("C grade")
elif  60<=marks<70:
    print("D grade")
elif  50<=marks<60:
    print("E grade")
elif  0<=marks<50:
    print("F grade")
else:
    print("Invalid marks")

# voting age
age = int(input("Enter voters age: "))
if 18 < age < 100:
    print("Eligible")
elif 0 <= age <= 18:
    print("not eligible")
else:
    print("Invalid age")

#checking if one number is multiple of another
n1 = int(input("Enter number one 1: "))
n2 = int(input("Enter number two 2: "))
if n2 % n1 == 0 or n1 % n2 == 0:
    
    if n2 % n1 == 0:
        print(f"{n2} is a multiple of {n1}")
    else:
        print(f"{n1} is a multiple of {n2}")

else:
    print("both are not multiples of each other")

    



