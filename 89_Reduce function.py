# #find the sum of all element present inside list without using lambda 
from functools import reduce
# def addall(x,y):
#     return x+y

# l=[1,2,3,4,5]
# data=reduce(addall,l)
# print(data)


# #find the sum of all element present inside list with using lambda 
# l1=[1,2,3,4,5]
# data=reduce(lambda x,y:x+y,l1)
# print(data)
# print(type(data))

# #find the product of all element present inside list with using lambda 
l1=[1,2,3,4,5]
# data=reduce(lambda x,y:x*y,l1,10)
# print(data)


# # find out the sum of all the elements from 1 to 100
# data=reduce(lambda x,y:x+y,range(1,101))
# print(data)


# #working with list which is containg string data 
# names=['surendra','priyanka','rahul','zini']
# data=reduce(lambda x,y:x+y,names,'hello')
# print(data)
# print(type(data))



# #working with dict 
# d={
#     1:'surendra',
#     2:'priyanka',
#     3:'rahul',
#     4:'zini'
# }
# data=reduce(lambda x,y:x+y,d.keys())
# print(data)
# 10
# d={
#     1:'surendra',
#     2:'priyanka',
#     3:'rahul',
#     4:'zini'
# }

# data=reduce(lambda x,y:x+y,d.values())
# print(data)


# reduce vs accumulate
from itertools import accumulate

l=[1,2,3,4,5]
print(list(accumulate(l,lambda x,y:x+y)))
print(reduce(lambda x,y:x+y,l1))
[1, 3, 6, 10, 15]


from itertools import accumulate

l=[1,2,3,4,5]
print(list(accumulate(l,lambda x,y:x*y)))
print(reduce(lambda x,y:x*y,l1))
[1, 2, 6, 24, 120]


# reduce will return different data type it depends what we are giving