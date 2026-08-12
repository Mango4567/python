#typecasting-process of converting one data type to another
#Expicit vs Implicit
#explicit first
name="Bro"
age=23 
gpa=1.9
student=True

age = float(age)
print(age)

gpa=int(gpa)
print(gpa)

student = str(student)
print(student)

name=bool(name)
print(name)
#implicit
x=2
y=2.0
x=x/y
print(x) #output will be float - small will be converted to big data type

