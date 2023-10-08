
'''Use of 'is' and 'in' '''
#---> they are used with list or when dealing with none or boolean datatype

# Vegetable shop Program

'''a=str(input("What do you want: "))
fruitlist=["apple","mango","guava","pineapple","melon","orange","grapes",]
veglist=["okra","chili","potato","spinach","cabbage","cauliflower"]

if(a=="fruits" or a=="fruit" ):
    fruit=input("Enter the fruit: ")
    if(fruit in fruitlist ):
	    print("\tAvailable")
    else:
	    print("\tNot Available")


if(a=="vegetables" or a=="vegetable"):
	vegetable=input("Enter the vegetable: ")
	if(vegetable in veglist):
		print("\tAvailable")
	else:
		print("\tNot Available!")


'''
# Another try-->better try


fruitlist={
	
"orange":"Available",
"mango":"Available",
"gauva":"unAvailable",
"apple":"Available",
"pineapple":"Available",
"papaya":"Available",
"melon":"Available",
"banana":"Available"

}

veglist={
"okra":"Available",
"chili":"Available" ,
"potato":"Available" ,
"spinach":"Available" ,
"cabbage":"Available" ,
"cauliflower":"Available"	
}


a=int(input('''Click:
	1.vegetables
	2.Fruits
	''' ))

if(a==2):
	print(fruitlist.keys())
	desired_fruit=input("Enter your Fruit: ")
	k=fruitlist.get(desired_fruit)
	if(k is None):
		print("Fruit Not Listed")
	else:
		print(fruitlist.get(desired_fruit))
elif(a==1):
	print(veglist.keys())
	desired_veg=input("Enter the vegetable: ")
	l=veglist.get(desired_veg)
	if(l is None):
		print("Vegetable Not Listed")
	else:
		print(veglist.get(desired_veg))
else:
	print("Invalid Command")
	






