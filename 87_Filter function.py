
# find even from a list wwithout using lambda
# def checkeven(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# l=[10,20,55,60,44,100]
# data=filter(checkeven,l)
# print(type(data))
# for i in data:
#     print(i)

# if u want to print without using loop then convert filter to any list ,set or tuple 

# find even from a list with using lambda
# l=[10,20,55,60,44,100]
# data=list(filter(lambda x:x%2==0,l))
# print(data)


# t=(10,20,55,60,44,100)
# data=list(filter(lambda x:x%2==0,t))
# print(data)


# t=(10,20,55,60,44,100)
# data=tuple(filter(lambda x:x%2==0,t))
# print(data)

# t=(10,20,55,60,44,100)
# data=set(filter(lambda x:x%2==0,t))
# print(data)


# write everything in one line 
# print(list(filter(lambda x:x%2==0,[10,20,55,66,123,99])))


# find out the common elements  from the 2 lists 
# a=[10,20,11,25,44,87]
# a=[1,20,258,25,44,89]

# data=list(filter(lambda x:x in a,l))
# print(data)

# filter out a name from list 
# name=['cj','raja','ad','jack','cj']
# data=list(filter(lambda x: x=='cj',name))
# print(data)


# with dictionary 

# d={
#     1:'cj',
#     2:'ak',
#     3:'ad',
#     4:'kk'

# }
# data=dict(filter(lambda x:x[0]%2==0,d.items()))
# print(data)

