#Python calculator

operator1 = float(input("ENTER YOUR FIRST NUMBER: "))
operation = input("ENTER YOUR OPERATION TO BE PERFORMED:(+,-,*,/): ")
operator2 = float(input("ENTER YOUR SECOND NUMBER: "))

if operation == "+":
    print(f"The Sum is:{operator1+operator2}")
elif operation == "-":
    print(f"The difference is:{operator1 - operator2}")
elif operation == "*":
    print(f"The Product is:{operator1 * operator2}")
elif operation == "/":
    print(f"The Divison is:{round(operator1 / operator2,3)}")
else:
    print(f"the {operation} is invalid!")