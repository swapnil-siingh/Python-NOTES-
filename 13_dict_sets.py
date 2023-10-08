  '''Dictionary and Sets'''
# dictionary is a collection of key value pairs
# mutable, indexed, unordered, no duplicate keys allowed


'''
dict={
	
"key1"="value1",
"key2"="value2",
"key3"="value3",

"anotherdict":{"key1"="value1",
               "key2"="value2",
               "key3"="value3", }


}'''


mydict={#declaring dictionary
	 # "keys" : "values",
	"swapnil" : "smart boy",#declaring keys and values comma is necessary after every value 
	"asus" : "smart laptop",
	"marks": [1,2,3,4],
	 1:2 ,  #integer key having integer value
	"anotherdict":{"boy":"swapnil", "player":"singh"}#declaring nested dictionary inside the previous one
 
}

print(mydict['anotherdict']['boy'])

mydict["swapnil"]="a smart boy"#changing the value of key"swapnil" in mydict
print(mydict['swapnil'])

print(mydict["swapnil"][1:3])#for printing a part of key value
print(mydict["swapnil"].replace("smart","cool"))#to replace the value of key
print(mydict["swapnil"].capitalize())#capitalize first index of key value
print(mydict["swapnil"].upper())#upppercase all values
print("\n\n\n",mydict["swapnil"].endswith("boy"))


print("\n\n\n",mydict.keys())#printing keys of mydict dictionary
print("\n\n\n",mydict.values())#printing values of mydict dictionary values


print("\n\n\n",type(mydict))#datatype of mydict
print("\n\n\n",list(mydict))#to list mydict as a list
print("\n\n\n",mydict.items())#to print (keys : values) for all values in mydict


# update method--> to add key:value in the existing dictionary or to update a key value
newdict={
	"lavish":"lifestyle",
	"wonderful":"people",
	"boy":"man"
}
mydict.update(newdict)
print("\n\n\n",mydict)
mydict.update({"movie":"a silent voice",26:11})#another way to write update command
print("\n\n\n",mydict)


'''-->Get method<--'''
'''
diff btw get and .[]---> below both command prints same output
still get is used? ---> if the value entered by the user is wrong in get command 
it prints none while .[] command returns error >> which becomes users responsibility to enter correct value 

--->get is used to prevent key error
''' 

print("\n\n\n",mydict["asus"])
print(mydict.get("asus"))
# print(mydict["asus2"])#here asus2 is not present in mydict. so this command returns error
print(mydict.get("asus2"))#while get command on execution return none(meaning:not present)


'''-->Sets<--'''
# sets is a collection of non repetitive elements
set1={1,2,3,4,5,1}#repeated values prints only 1 time
print("\n\n\n",set1)
print(type(set1))

emptyset={ }#this syntax will create empty dictionary not set
print("\n",emptyset)
print(type(emptyset))

#---> To create empty set 
#-->1
emptyset=set(emptyset)#-->empty dictionary get converted to empty set
print(type(emptyset))
#-->2
b=set()
print(type(b))

#--->To add elements in empty set or any set
b.add(4)#NOTE-> add command only takes one argument
b.add(5)#i.e. it can add only one element at a time
print("\n\n",b)

#>>>List or dictionary cannot be added in a set due to its unhashable type
b.add(1)
b.add(2)
b.add(3)
b.add(9)
#--->removing elements from set
b.remove(5)
print("\n\n",b)

#>>>pop -- removes any arbitary value from the set and prints it
print("\n\n",b.pop())#

#>>>clear -- empties the set
b.clear()
print("\n\n",b)

#>>>union -- union of two sets
print(b.union(set1))
print(b.union({"ram","shyam"},set1))

#>>>intersection -- intersection of sets i.e. common elements in sets
egset1={1,2,3,4,5,5}
egset2={"ram","ra",2,3}
egset3={2,"a0","a1","a2"}
print("\n\n",egset1.intersection(egset2,egset3))
