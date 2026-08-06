temp = 40
sunny = True
if temp<=0 or temp>=30:                #and - two conditions or more to be true
    print("the temperature is good",temp) #or - only one condition needs to be true
else:
    print("the temperature is bad")     #not- converts true to false or vice versa

if not sunny:           #sunny == "True"so we can shorten this to direct boolean value sunny
    print("the weather is sunny")
else:
    print("it is cloudy outside")