# to make a set from different iterable items like list tuple range 

# normal method 
l=[1,2,35,6,36,9]
s=set()

for i in l:
    s.add(i)
print(s)

# from list
l=[1,2,35,6,36,9]
s={i for i in l}
print(s)

# l=[1,2,35,6,36,9]
# s={i*2 for i in l}
# print(s)

# name=['chinmay','raja','rahul','loli' ]
# s={i[0] for i in name }
# print(s)

# name=['chinmay','raja','rahul','loli' ]
# s={i if i!='raja' else 'raaj' for i in name }
# print(s)

# # from range 
# s={i for i in range(10)}
# print(s)

# s={i for i in range(20,41) if i%4==0}
# print(s)