
age = int(input("ENTER YOUR AGE: "))

if age >= 18:
    print("You are now Eligible!")
elif age <= 0:
    print("You are not born yet")
elif age >= 100:
    print("Ypu are too old to sign up")
else:
    print("You must be 18+ to be Eligible!")

response=input("Would You like Food?(Y/N): ")

if response =="Y" or response == "y":
    print("Have Some Food")
else:
    print("No Food for you!")

name = input("Enter Your Name: ")

if name == "":
    print("TYPE SOMETHING YOU USER!")
else:
    print(f"Hello {name}")

is_online = False

if is_online:
    print("You Are Online")
else:
    print("You Are Not Online")