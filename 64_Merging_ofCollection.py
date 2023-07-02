#Merging of collections 
#  list merging 
l=[10,20,30,40,50]
s=[100,200,'chinmay']
z=l+s
print(z)

# l=[10,20,30,40,50]
# s=[100,200,'chinmay']
# z=[*l,*s]
# print(z)

# *l *s means all the element of l and s


#tuple merging 
# l=(10,20,30,40,50)
# s=(100,200,'chinmay')
# z=l+s
# print(z)

#set merging
# s1={10,20,30,40}
# s2={50,'chinmay',100}
# s3=s1+s2  #TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(s3)

# solution 
# s1={10,20,30,40}
# s2={50,'chinmay',100}
# s3={*s1,*s2}
# print(s3)

d1={1:'chinmay',2:'raja'}
d2={3:'biki',4:'mani'}

d3={*d1,*d2}
print(d3)
# you will get only keys here
#solution

# d1={1:'chinmay',2:'raja'}
# d2={3:'raja',4:'chinmay'}

# d3={**d1,**d2}
# print(d3)