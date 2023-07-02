# add 4 to each element  without using map and lambda


# l=[10,20,30,40]
# l1=[]
# for i in l:
#     i+=4
#     l1.append(i)
# print(l1)

# add 4 to each element  without using  lambda
# def add4(x):
#     return x+4

# l=[10,20,30,40]
# data=list(map(add4,l))
# print(data)

# add 4 to each element  with using  lambda
# l=[10,20,30,40]
# data=list(map(lambda x:x+4,l))
# print(data)

# find the square without using map and lambda
# l=[10,20,30,40]
# l1=[]
# for i in l:
#     i=i*i
#     l1.append(i)
# print(l1)

# find the square with using map and lambda
# l=[10,20,30,40]
# data=list(map(lambda x:x*x,l))
# print(data)

# add all the element of one list with another list without map and lambda
# l1=[10,20,25,45]
# l2=[25,66,23,41]
# data=list(map(lambda x,y:x+y,l1,l2))
# print(data)
# but the length of all the list must b same

# find the length of the string in the list 
l=['name','chinmay','jyotishi']
data=list(map(lambda x:len(x),l))
print(data)