# creation of a tuple in different ways
# create an empty tuple
# t=()
# print(t)
# print(type(t))

# creating with a single value 
# t=(230)  #without comma it will be treated as int 
# t1=(230,)  #with comma it will be treated as tuple 
# print(t)
# print(t1)
# print(type(t))
# print(type(t1))


# creating tuple with different datatype
# t=(21,25,'chinmay',45.2,True)
# print(t) 

#creating tuple withput ()
# t=21,35,'chinmay',False
# print(t)
# print(type(t))

# creation of tuple using tuple()

# l=[10,2,45,85,6]
# t=tuple(l)
# print(t)

# l=tuple(range(11))
# print(l)

# t=tuple('chinmay')
# print(t)



# t=(10,20,12,3,2,5)
# t[1]=849
# print(t)  #it will through an error bcoz it is immutable

#  SOME OPERATIONS IN TUPLE
# +
# l=10,203,58,12,32,8
# l1=12,8,56
# print(l+l1)

# *
# l=54,58,89,25
# print(l*5)  #it will print 5times

# traversing in the tuple 
# t=(10,20,32,2255,669)
# for i in t:
#     print(i,end=" ")

# i=0
# while i<len(t):
#     print(t[i])
#     i=i+1

# tuple packing 
# a=12
# b=25
# c=58
# d=98
# t=a,b,c,d
# print(t)

# tuple unpacking
# t=(12,25,36,698)
# a,b,c,d=t
# print(a,b,c,d) 

# tuple returning by using function
# def fun():
#     l=[10,20,35,36,8]
#     return(l[0],l[2])
# t=fun()
# print(t)

# nested tuple 
# t=((120,25,5),25,58,(25,89))
# print(t)

# you can add a list inside a tuple
# t=(10,25,65,9,[10,25,9,88])
# print(t)
# print(t[4])
# t[4][1]='cj'
# print(t[4])
