#format specifiers ;- {value:flags} formats a value based on flags inserted

price1 = 3000.1459
price2 = -98700.65
price3 = 12000.34

print(f"Price1 is ${price1:+,.2f}")
print(f"Price2 is ${price2:+,.3f}")
print(f"Price3 is ${price3:+,.3f}")