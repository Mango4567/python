#compound interest calculator
principal = 0
rate = 0
time = 0


while True:
    principal = float(input("Enter your new principal amount: "))
    if principal < 0:
        print("Principal amount can't be small")
    else:
        break
    
while True:
    rate = float(input("Enter your rate of interest: "))
    if rate < 0:
        print("rate can't be small")
    else:
        break

while True:
    time = float(input("Enter your time in years: "))
    if time < 0:
        print("time can't be small")
    else:
        break

print(principal)
print(rate)
print(time)

total = principal*(1 + rate/100)**time #or pow((1 + rate/100),time)
print(f"Balance after {time} is : {total:.2f}")