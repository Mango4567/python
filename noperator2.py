import math
friends=10
#friends = friends + 1
#friends+=1
#friends -= 2
#friends *= 2
#friends/= 2
#friends**=2
#friends %= 2

print(friends)

x = 3.14
y = -4
z = 5
#result = round(x)
#result = abs(y) #always +ve
#result = pow(4,3) #4*4*4
#result = max(x,y,z)
#result = min(x,y,z)
#print(result)

#next

#print(math.pi)
#print(math.e)
#result =math.ceil(x) #3.1=4
#result = math.floor(x)#

#area = math.pi*pow(radius,2)
#circumference = 2*math.pi*radius
#print(f"The Area of a circle is:{round(area,3)}cm^2")
#print(f"the circumference of the circle is:{round(circumference,2)}cm")

a = float(input("Enter the value of side a of right angled traingle: "))
b = float(input("Enter the value of side b of a right angled triangle: "))

#c = math.sqrt(a*a+b*b)
c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The hypotenuse value is: {round(c,2)}")
