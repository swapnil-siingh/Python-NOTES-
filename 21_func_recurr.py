'''Functions'''
# Group of statements performing a specific task
# def percentage(mk):
# 	return ((mk[0]+mk[1]+mk[2]+mk[3])/4)

# mak1=[45,45,32,65]
# percentage1=percentage(mak1)

# mak2=[67,88,99,54]
# percentage2=percentage(mak2)

# swa=[67,87,98,66]
# percentage3=percentage(swa)
# print(percentage1,percentage2,percentage3)


'''Types of functions'''
# Built in functions-->Already present in python
# User defined functions-->defined by user
# Examples of built in functions
# len(),print(),range() 

# user defined functions
a=int(input("Enter your Number: "))
b=int(input("Enter your Number: "))
def sum(num1,num2):
	return num1+num2
s=sum(a,b)	
print("Sum is: ",s,"\n")

#--Default parameter value
def greet(name="stranger"):#here stranger is a default value for name 
	print("good day",name) #it get called whenever no argument is given

greet("swapnil")
greet()	


'''--Recursion--'''
# a function calling itself -->it is used to use mathematical formula as a function
def factorial_recur(n):
	if n==1 or n==0:
		return 1
	else:
		return n*factorial_recur(n-1)

a=factorial_recur(5)
print(a)		




