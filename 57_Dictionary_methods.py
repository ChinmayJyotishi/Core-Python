# get()

# d={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }
# print(d.get(1))
# print(d.get(3))

# print(d.get(999))  #it will not give u keyerror it will give u none value
# print(d[999]) #it will give u a key error

# print(d.get(999,'unknown key'))
# u can change the none value to string u needed
# print(d.get(1,'unknown key')) #if the key is present then it will not show u the string

# items()
# d={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }
# print(d.items()) #it will return a list of tuple
# items means both key and value

# to print line by line

# for i in d.items():
#     print(i)

# for i,j in d.items():
#     print(i,'  ' ,j)


# pop()
# d={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }
# print(d)
# print(d.pop(1))
# print(d)
# print(d.pop()) #in dictionary if u are not passing the argument the u will get keyerror


# popitems()
# d={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }
# print(d.popitem()) #it will remove the last inserted item and return the key as well as value in the form of tuple
# print(d)

# if the dict is empty then it will give u key error

# keys()
# d={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }
# print(d.keys()) #it will return all the keys in the form of list of tuple

# for i in d.keys():
#     print(i)

# value()
# d={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }
# print(d.values())


# for i in d.values():
#     print(i)

# setdefault()
# d={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }
# print(d.setdefault(5,'cj'))
# print(d)
# if the key and value is not available then it will return the value and add the key and value to dict

# print(d.setdefault(1,'cow')) #if the key is present then it will not add the key and the value of that key means 1's value

# update()
# d1={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }
# d2={
#     11:'one ',12:'two',13:'three'
# }
# d1.update(d2)
# print(d1)

# but if the keys are same in  both dict then it will update the values
# d1={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }
# d2={
#     1:'one ',12:'two',13:'three'
# }
# d1.update(d2)
# print(d1)


# copy()
# d1={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }

# d2={
# }
# d2=d1.copy()
# print(d2)

# clear()
# d1={
#     1:'tiger',2:'lion',3:'wolf',4:'deer'
# }
# d1.clear()
# print(d1)

# formkeys()
# if u want to create a dictionary from iterable object then u can use formkeys

# l=[12,13,14,15]
# d=dict.fromkeys(l) #it will take the list as the keys and none as values\
# print(d)

# l=[12,13,14,15]
# d=dict.fromkeys(l,'hello') #it will take hello as values
# print(d)

# l=[12,13,14,15]
# d=dict.fromkeys(range(10),'cj') #it will take cj as values
# print(d)

# d1={}
# d2=[12,55,69,36,24,4,5]
# d1.update(d2)

# print(d1)

# with innerable obj 
# r=range(5)
# l=[1,2,3]
# d=dict.fromkeys(r,l)
# print(d)

# r=range(5)
# l=[]
# d=dict.fromkeys(r,l)
# print(d)

# # r=range(5)
# l=[]
# d=dict.fromkeys(l,l)
# print(d)



# for i in students:
#     for j in students.keys():
#         print(j,i[j])
