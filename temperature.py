unit = input("Enter the temperature in Celsius or Farehnite (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp*9/5)+32
    unit = "Farenheit"
    print(f"The converted temperature is: {round(temp,1)} {unit}")
elif unit == "F":
    temp = (temp-32)*5/9
    unit = "Celsius"
    print(f"The converted temperature is: {round(temp,1)} {unit}")
else:
    print(f"The {unit} is invalid!.Please re-enter the correct one")

