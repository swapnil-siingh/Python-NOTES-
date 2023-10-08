'''Programs Using Conditional Expression'''

# Program 1--> greatest of four numbers

# a=int(input("Enter First Number: \n"))
# b=int(input("Enter second Number: \n"))
# c=int(input("Enter third Number: \n"))
# d=int(input("Enter fourth Number: \n"))

# if(a>b and a>c):
# 	if(a>d):
# 		print("First number is greatest")
# 	else:
# 		print("Fourth number is greatest")
# elif(b>c and b>d):
# 	print("second number is greatest")
# elif(c>b and c>d):
# 	print("third Number is greatest")
# else:
# 	print("fourth Number is greatest")


# Program 2--> Check whether the students is passed or failed

# sub1=int(input("Enter Maths Score: "))
# sub2=int(input("Enter physics Score: "))
# sub3=int(input("Enter chemistry Score: "))
# totalper=int((sub3+sub2+sub1)/3)

# if(sub1<33):
# 		    print("Failed in Maths")
# if(sub2<33):
# 		    print("Failed in Physics")
# if(sub3<33):
# 		    print("Failed in chemistry")	

# if(sub1<=100 and sub2<=100 and sub3<=100):
# 	print("You scored ",totalper,"Percent Marks")
# 	if(sub1>=33 and sub2>=33 and sub3>=33 ) :
# 		if(totalper>=40):
# 			print("Qualified")
# 		else:
# 			print("Not Qualified")		
# 	else:
# 		print("Not Qualified")
# else:
# 	print("Marks Cannot exceed 100")



#Program 3--> to print 'eligible' if the age entered is greater than or equal to 18

# age=int(input("Enter your Age: "))

# # using nested if conditions

# if(age>=18):
# 	if(age>110):
# 		print("Age Over Limit!!")
# 	else:
# 		print("You are Eligible")
# if(age<18):
# 	print("Not Eligible!")

# # using logical operators

# if(age>=18 and age<=110):
# 	print("\n\nYou are Eligible!")
# else:
# 	print("\n\nNot Eligible")



# Program 4--> to check whether the entered text is spam 

# text=input("Enter your text: ")

# if("make money" in text):
# 	spam=True
# elif("subcribe this" in text):
# 	spam=True
# elif("click this" in text):
# 	spam=True
# elif("free gifts" in text):
# 	spam=True
# elif("watch this" in text):
# 	spam=True
# else:
# 	spam=False

# if(spam):
# 	print("Spam Comment")

# else:
# 	print("Not a Spam")	

# Program 4-->to check whether username contains less than 10 characters

# a=len(input("Enter Your Username: "))
# if(a<=10):
# 	print("Valid Username")
# else:
# 	print("Invalid Username")


# Program 5-->to check the name is in list on not

# avengers=["thor","ironman","captain america","hawkeye","black widow","hulk"]
# villain=["thanos","ironmonger","mandarin","loki","mysterio","redskull"]
# name=input("Enter your Name: ")
# if(name in avengers):
# 	print("Avengers Assemble")
# elif(name in villain):
# 	print("Villain Found")
# else:
# 	print("Invalid")


# Program 6-->to print grade corresponding to the marks
# maths=int(input("Enter Maths Marks: "))
# chemistry=int(input("Enter chemistry Marks: "))
# physics=int(input("Enter physics Marks: "))
# totalper=(maths+physics+chemistry)/3


# if(totalper<=100 and totalper>=91):
# 	grade="Ex"
# elif(totalper>=81):
# 	grade="A"
# elif(totalper>=71):
# 	grade="B"
# elif(totalper>=61):
# 	grade="C"
# elif(totalper>=51):
# 	grade="D"
# else:
# 	grade="F"

# print("Grade:",grade)