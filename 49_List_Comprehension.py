# if u want to create a list from iterable obj like lits tuple range dict etc by writing very less number of code in effecient way we can go for list comprehension

# l=[ i   for i in range(11)]
# print(l)

# l=[ i*i  for i in range(11)]
# print(l)

# l=[ i+10  for i in range(11)]
# print(l)

# l=[ i for i in range(1,21) if i%2==0]
# print(l)

# names=['chinmay','rahul','jatin']
# l=[i for i in names]
# print(l)


# names=['chinmay','rahul','jatin']
# l=[i[0] for i in names]
# print(l)

# create a list having 'a' letter
# names=['chinmay','rahul','jatin','sili']
# l=[i for i in names if 'a' in i]
# print(l)

# names=['chinmay','rahul','jatin','sili']
# l=[i[1:4] for i in names if 'a' in i]
# print(l)

# names=['chinmay','rahul','jatin','sili']
# l=[ i  if i!='rahul' else 'hii' for i in names]
# print(l)

# # create a list from tuple
# T=(10,20,30,24,20)
# l=[i for i in T]
# print(l)

# T=(10,20,30,25,20)
# l=[i  for i in T if i%2==0]
# print(l)

# # create a list from string 
# name="Chinmay"
# l=[i for i in name]
# print(l)

# name="Chinmay"
# l=[i for i in name[1:4]]
# print(l)

# l=[[j for j in range(3) ] for i in range(3)]
# print(l)


x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
print(list[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if x+y+z!=n)

# for i in range(2):
#     print('i=',i)
#     for j in range (2):
#          print('j=   ',j)
#          for k in range(2):
#             print('k=   ',k)
     