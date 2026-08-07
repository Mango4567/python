#collections-single "variable" used to store multiple values
#list-[]-> ordered and changeable elements,Duplicates ok
#tuple-()->ordered and unchangeable,Duplicates OK ,FASTER
#sets-{}-> unordered and immutable , but Add/Remove OK , duplicates not allowed

#fruits = ["apples","oranges","bananas","Coconut"] ->lists
#fruits = {"apples", "oranges","bananas","coconut"}->sets
fruits = ("apples","raspberry","pie","coconut") 
#print(fruits[0])

#for fruit in fruits:     #i,x ki place mein fruit name use ksrte hai counter mein
    #print(fruit)
#print(dir(fruits)) or print(help(fruits))

#print(len(fruits))
#print("apple" in fruits)
#fruits[0] = "pineapple" #changing the element of a list
#fruits.append("pineapple") #adding to the end of a list
#fruits.remove("bananas") #removing the specified element
#fruits.insert(0,"grapes") #inserting a value to the specified index
#fruits.sort()
#fruits.reverse()
#print(fruits.index("grapes"))
#print(fruits.count("grapes"))


#print(fruits[0])
#for fruit in fruits:     #i,x ki place mein fruit name use ksrte hai counter mein
 #   print(fruit)
#fruits.add("greenapple")

#fruits.remove("apples")
#print(fruits) 

print(fruits)