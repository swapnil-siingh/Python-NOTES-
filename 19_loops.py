'''Loops'''

# Loops tells the computer , which set of instructions to repeat 

# Types->
# >>while 
# >>for


'''>>While Loop<<'''
# syntax
# while condition :
	# body of loop
# --->while loop continues executing till the condition becomes false

#Program 1:Using while loop print numbers from 1 to 50
# i=1
# while i<=50:
  # 	print(i)
# 	i+=1

#Program 2:Printing name 5 times
# i=0
# while i<5:
# 	print("swapnil")
# 	i+=1
# print("done")	#done get printed when the condition of loop fails 

# Program 3:printing content of a list using while loop
# i=0
# fruitlist=["mango","grapes","apple","pineapple"]
# while i<len(fruitlist):
# 	print(fruitlist[i])
# 	i+=1

  

'''>>For Loop<<'''
# syntax
# for condition:
	# body
# --->it is used to iterate through a sequence like list,tuple etc

# Program 1:printing content of a list using for loop
# fruitlist=["mango","grapes","apple","pineapple"]

# for items in fruitlist:
# 	print(items)


'''Range function in python'''
# It is used to print a sequence of numbers
# User can specify the start , stop and step size of the sequence
# (start,stop,step-size)

# Program 2:Printing sequence using range
# for i in range(8):       #prints from 0 to 7(n-1)
# 	print(i)
# print("\n")
# for i in range(1,8,2):   #print from 1 to 7 missing every second digit
# 	print(i)


# --->>for with else-optional else can be used with 'for statement' 
'''why else? else statement is executed by the compiler only if termination of loop 
   is successful that is loop is not forcefully terminated by break statement.while
   simple print statement still gets executed.'''
# example program-->
# for i in range(8):
# 	print(i)
# 	if i==5:
# 		break
# else:                
# 	print("done")	#here else statement is not executed 
# print("done")       #while print statement still executes
# 	

''' --->break statement ---> to terminate the loop 
 --->continue statement --->to skip the current iteration and continue with the next one'''
# example program-->
# for i in range(10):
# 	if i==2 or i==5:
# 		continue    #this skips 2 and 5 from the sequence
# 	print(i)


'''Pass Statement'''
# It is a null statement in python . It instructs the program to do nothing
# Program-->Here program doesn't throw error as pass statements nullify all conditions
# a=3
# if a<0:
# 	pass
# 	for x in range(10):
# 		pass
# 		