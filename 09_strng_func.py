  '''Strings'''

#-->Datatype in python
#-->Declaration 
    
print('hello world')        #single quoted
print("hello world")        #Double quoted
print('''Hello world''')    #triple quoted


a=''' hello world'''
print(a)


# To concate two strings
greeting="Good morning "
name="swapnil "
c=greeting+name
print(greeting + name)
print(c)


'''String Slicing'''
# S W A P N I L    string
# 0 1 2 3 4 5 6    indexing
#-7-6-5-4-3-2-1    negative indices used to acces the string from behind when the length is not known

print(name[0])#value of index 0 gets printed
print(name[1])#value of index 1 gets printed


# slicing
print(name[0:3])#index 0 to 3 get printed excluding 3 index
print(name[0:7])#index 0 to 7 get printed excluding 7 index


print(name[:4])#it automaticaly repalces the empty value with the minimum value i.e 0
print(name[1:])#same as name[1:7] replace the empty value with max value


print(name[-5:-1])#same as name[2:7]

# slicing with skip value
name="swapnil is smart boy"
print(name[1:9:2]) #it skips every 2nd character  from index 1 to 9(excluded) 
print(name[0:15:4])#it skips every 4th character


'''String Functions'''
string="once upon a time in mumbai there lived a man"

# length function - to print the length of a string
print(len(string))

# endswith function - to check whether the string endswith desired result
print(string.endswith("man"))#true as string endswith man
print(string.endswith("boy"))#false as string endswith man

#count - to count the occurrence of any character or string
print(string.count("o"))
print(string.count("a"))

#capitalize - makes first character capital
print(string.capitalize())

# find function - to find the index of string or character(first occurrence) 
print(string.find("upon"))
print(string.find("upn"))#prints -1 as upn is not present in string 

# replace function - to replace old word with a new word
print(string.replace("upon","there was"))
string=string.replace("once","idiot")
print(string)
'''Escape sequence characters'''
# \\ - for backslash
# \n - for new line
# \t - for white space
# \' - for double quotes
# single \ cannot get printed
print("H\e is\\ a g\tood boy.\nHe is a \'bad boy")

# fstring function - to avoid using str statement again and again.variable are declared in {}
a=3
b=2
print(f"\nMultiplication of {a} and {b} is {a*b}")#another way to write print statment 


# startswith function - to check whether the string starts with a particular result
print(string.startswith("idiot"))

# end function - to avoid new line to add at end of a string
print("hello",end=" * ")       #here every word has * between them 
print("world",end=" * ")       #and all are in single line 
print("how",end=" * ")         #while without end
print("are you",end=" * ")     #every thing prints in different lines


# strip function - to strip the unnecessary space in a string
sentence="\n       wonderful day,  today is   "
print(sentence)
print(sentence.strip())


# lower function - to print data in lower case
a="Hello THIS IS a program"
print(a.lower())