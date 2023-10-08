  # Program 1-->Greet a user using functions
# def greet(name):
# 	print("Good Day "+name)

# greet("swapnil")

# Program 2-->Greatest of three numbers
# def greatest(a,b,c):
# 	if a>b and a>c:
# 		return a
# 	elif b>a and b>c:
# 		return b
# 	else:
# 		return c	

# a=int(input("Number is : "))
# b=int(input("Number is : "))
# c=int(input("Number is : "))
# k=greatest(a,b,c)
# print("greatest is: ",k)

# Program 3-->To convert farenheit into celsius
# def celcius(f):
# 	return (f-32)*(5/9)
# a=int(input("Temperature in Fareheit is : "))
# b=int(celcius(a))
# print("Temperature in celcius is ",b,"degrees")

# Program 4-->To print sum of natural numbers using recursive function
# n=int(input("Number is: "))
# def sum(n):
# 	if n<1 or n==0:
# 		return 0
# 	else:
# 		return n+sum(n-1)

# a=sum(n)
# print(a)

# Program 5-->Function to print * pattern
# def star(n):
# 	while n>0:
# 		print("*"*n)
# 		n-=1


# a=int(input("Enter Numbers: "))
# star(a)

# Program 6-->function to remove a word from string and strips the string 
# def remove(string,word):
# 	newstr=string.replace(word,"")
# 	return newstr.strip()


# string="          Such a wonderful weather       "	
# a=remove(string,"such")
# print(a)