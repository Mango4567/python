# Weight convertor

weight = float(input("enter your weight: "))
unit = input("Kilograms or Pounds?:(K/L): ")

if unit == "K":
    weight = weight*2.205
    unit = "lbs"
    print(f"Your weight in kgs is:{round(weight,1)} {unit}")
elif unit == "L":
    weight = weight/2.205
    unit = "kgs"
    print(f"Your weight in kgs is:{round(weight,1)} {unit}")
elif weight <= 0:
    print("INVALID WEIGHT!")
else:
    print(f"the {unit} is not Valid!")

print(f"Your Weight is: {round(weight,1)} {unit}")