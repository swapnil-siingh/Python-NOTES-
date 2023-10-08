'''---:>Working dictionary<:---'''
hindidict={
	
	"jaana":"Go",
	"insaan":"human",
	"jadugar":"magician",
	"dabba":"box",
	"sabzi":"vegetable"

}
print("Search meaning of these Words: ",hindidict.keys())
a=input("Enter the Word: ")

# print(hindidict[a])---> This will return error on wrong entry so it is avoided and get() is used
print(hindidict.get(a))

