'''Conditional Expressions'''

"""if and elif"""
# Syntax
'''

if(condition):
    statement
elif(condition):
    statement
else(condition):
    statement

'''
# example

a=input("enter your values: ")
b=input("enter your values: ")

# 'if-else' ladder program--> conditions are checked from if to else

if(a<b) :                                     #if first condition fails 
	print("b is greater than a")
elif(a==b):                                   #compiler jumps to second
	print("both are equal")
else:                                         #if all conditions are true only
	print("a is greatest")                    #the first statement is executed


# Multiple 'if' program--> all if statements are checked and true conditions are executed

if(a<=b) :
	print("a is less than b")
if(a>=b) :
	print("b is less than a")
if(a==b):
	print("both are equal")