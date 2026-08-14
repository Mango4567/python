#To check Whether a number is positive or negative
number = float(input("Enter a number to check: "))
if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
elif number == 0:
    print("Number is strictly zero")
else:
    print("invalid input")

#To check if a number is divisible by 5
number = float(input("Enter a number: "))
print("number is divisible by 5") if number % 5 == 0 else print("number is not divisible by 5")

#to check if a number is divisible by both 3 and 5
number = int(input("Enter a number: "))
if number < 0:
    print("RE-Enter the number: ")
else:
    if number % 3 and number % 5 == 0:
        print("NUmber is divisible by both")
    elif number % 3 == 0 and number % 5 != 0:
        print("Number is only divisble by 3")
    elif number % 3 != 0 and number % 5 == 0:
        print("Number is only divisible by 5 ")
    else:
        print("Invalid input, please re-enter")
