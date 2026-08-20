#name = input("Enter your full name: ")
#phone_number=input("Enter your phone number: ")
#print(len(name)) used for printing the length
#print(name.find("B")) #.find()-> finds the first occurence of the string
#print(name.rfind("c"))#.rfind()->finds the last occurence of string
#print(name.capitalize())#capitalises the first letter
#print(name.upper())#capitalises whole string
#print(name.lower())
#print(name.isdigit())#returns true if all  characters instrings are numbers
#print(name.isalpha())#returns true if all  characters instrings are alphabets
#print(phone_number.count("-"))#counts the occurences of the specified character
#print(phone_number.replace("-","+"))# used for replacing specified character
#print(help(str))
#validate username
#username is no more than 12 characters+username must not contain spaces and digits
username = input("Enter your username: ")

if len(username)>15:
    print("Please RE-Enter username with 15 characters!")
elif not username.find(" ")==-1:
    print("username contains spaces")
elif not username.isdigit():
    print("username cant have digits")
else:
    print(f"Welcome!{username}")
