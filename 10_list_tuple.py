'''Lists and Tuples'''

# list indexing starts from 0

a=[1,4,3,5,"2","ada"]
a[2]=34#list elements can be changed
print(a)
print(a[2])
print(a)
# List Slicing

print(a[1:3])    
print(a[:3])
print(a[4:])
print(a[1:6:2])#skip index
print(a[-4:-1])#accessing from behind

'''List Methods'''

l1=[11,5,9,54,4,1,8]

# --sort--
print(l1)
l1.sort()#sorts the list 
# li_sorted=l1.sort()->sort command works indivisually. cannot be stored in another variable
print(l1)

# --reverse--
l1.reverse()#reverses the list
print(l1)

# --Append--
l1.append(65)#adds at the end of list
print(l1)

# --insert--
l1.insert(1,999)#inserts 999 at index 1 
        # ^  ^
     # index value 
print(l1)

# --pop-- 
l1.pop(2)#deletes value at index 2
print(l1)

# --remove--
l1.remove(999)#removes 999 from the list
print(l1)

#--sum--
# print(sum(l1)) both ways are correct
l1=sum(l1)

'''Tuple'''
# data cannot altered once input
# it is a inmutable datatype in python

# defing a tuple
t1=() #empty tuple
t2=(1)#wrong way to declare a tuple ,it is a variable will value 1
t3=(2,)#correct way
t4=(3,4,5)
print(t1)
print(t2)
print(t3)
print(t4)

#-->Tuple methods<--
tuple1=(1,2,4,5,2,1,5,7,2,9,1,4)
# count -- counts the numbers of occurence
print(tuple1.count(1)) #or tuple1=tuple1.count(1) and then print(tuple1) this can also be used
print(tuple1.count(2))

#index -- searches the first ocurring index of searched value
print(tuple1.index(1))
print(tuple1.index(2))
