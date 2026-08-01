name=input("Enter your name:")
age=int(input("Enter your age:"))
age=age+1

print(f"Hello {name}")
print(f"You are {age} yaers old")
#mad libs
adjective1=input("Enter an Adjective:")
noun=input("enter a noun:")
verb=input("enter a verb:")
adjective2=input("enter second adjective:")
adjective3=input("enter third adjective:")
print(f"Today we are going to {adjective1} zoo")
print(f"ian an exhibit,I saw a {noun}")
print(f"{noun} and {adjective2} and {verb}ing")
print(f"I was {adjective3}")
#shopping cart
item=input("Enter the Item you want to buy:")
price=float(input("what is the price:"))
quantity=int(input("How many would you like:"))

total=price*quantity

print(f"you have bought {quantity} x {item}/s")
print(f"Your total is:{round(total,2)}")