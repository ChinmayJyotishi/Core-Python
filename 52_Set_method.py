# add
# it will add a single element
# s={12,5,65,9,8,669}
# s.add(89)
# print(s)

#if same element then it will not be reflected

# s={12,5,65,9,8,669}
# s.add(669 )
# print(s)

# to add multiple element use update
# s={12,5,89,5,687}
# l=[12.66,548,98,99,8]
# s.update(l)
# print(s)

# in update you have to pass iterable object not only int 
# s={78,25,69,36,8}
# s.update(888,898) #this will not add as it is not a iterable item like list or ranges

# remove 
# s={12,6,69,89,59}
# s.remove(89)
# print(s)

# if your key is not present the it will show key error 

# discard 
# it is also like remove but here if your key element is not present then it will not through any error
# s={12,6,69,89,59}
# s.discard(155)
# print(s)

# pop()  it will delete any random value and it is returning

# s={7889,56,74}
# s.pop()
# print(s)

# s={45,89,78,25}

# print(s.pop())  #it will return that deleted value

# copy() 
# shallow copy--means any changes made in old or new set it will not reflect to any one and the id's are different

# s1={45,99,56,41,58,}
# s2=s1.copy()
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))

# s1.add(98989)
# print(s1)
# print(s2)

# deep copy 
# opposite of shallow copy 

# s1={45,99,56,41,58}
# s2=s1  #assign
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))

# clear --it will clear all the elements of a set
# s={10,20,25,669,36}
# s.clear()
# print(s)

# enumerate()

# s={10,25,65,99,95,36}
# for i in enumerate(s):
#     print(i)


# s={10,25,65,99,95,36}
# print(min(s))
# print(max(s))

# sum()
# s={10,25,65,98,96,660}
# print(sum(s))

# s={10,25,65,98,96,66}
# print(sorted(s))
# print(sorted(s,reverse=True))