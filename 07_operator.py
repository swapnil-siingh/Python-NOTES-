 '''operators'''
# Arithmatic operators  (+-*/)
a=3
b=4
s1=a+b
s2=a-b
s3=a*b
s4=a/b

print("the value of a+b is:" ,a+b)         #different ways of
print("the value of a+b is:" ,3+4)         #printing the sum
print("the value of a+b is:" ,a+b,3+4)     #of two numbers
print("the value of a+b is:" ,s1)
print("the value of a+b is:" ,s2)
print("the value of a+b is:" ,s3)
print("the value of a+b is:" ,s4)

#Assignment operators (=,-=,+=)
a=34
a+=2
a-=4
a*=1
a/=2
print(a)

#Comparison operators (|<| |>| |>=| |<=| |==| |!=|)
c=(b> a)
c=(4>=2)
c=(4==3)
c=(4!=3)
print(c)

#Logic operators (|and| |or| |not|)
bool1=True
bool2=False
print("the value of bool1 and bool2 is : ",(bool1 and bool2)) # they can be used 
print("the value of bool1 or bool2 is : ",(bool1 or bool2))   # as truth table of
print("the value of not bool2 is : ",(not bool2))             # and or not
print("the value of not bool1 is : ",(not bool1))  


