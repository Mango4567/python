#larger of two numbers
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
if num_1 > num_2:
    print("number1 is greater")
elif num_2 > num_1:
    print("number2 is greater")
else:
    print("Both numbers are equals")

#largest of three numbers
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if (a>b) and ((b>=c) or (c>=b)):
    print("a is largest of three:",a)
elif (b>a) and ((a>=c) or (c>=a)): 
    print("b is largest of three:",b)
elif (c>a) and ((a>=b) or (b>=a)):
    print("c is largest of three:",c)
elif a==b==c:
    print("there is no largest number among them:",a,b,c)
else:
    print("invalid output")

#temperature checker
temp = int(input("Enter the temerture in Celsius: "))
if (0<=temp<=15):
    print("it is cold")
elif (16<=temp<=30):
    print("it is warm")
elif (31<=temp<=60):
    print("it is hot")
else:
    print("Temperature is not in range, please reenter in the range")

#tocheck whether a charctwr is vowel or consonant
char = input("Enter a character form (A-Z): ").lower()  # char is not inbuilt in python , it is string with character of length 1
if char in ["a","e","i","o","u"]:
    print("TEXT ENTERED IS A VOWEL")
else:
    print("TEXT ENTERED IS A CONSONANT") 

#TO check whether a charcater is uppercase ,lower case, digit or special character
charc = input("ENTER CHARACTER TO BE EVALUATED: ")
if "A"<= charc <="Z"or"a"<= charc <="z":   #can be simplified using isalpha(),isdigit()
    print("TEXT IS ALPHABET")
elif "0"<= charc <="9":
    print("TEXT IS NUMBER")
else:
    print("TEXT IS SPECIAL CHARACTER")

