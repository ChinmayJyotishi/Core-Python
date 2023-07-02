# creating frozenset 
# frozenset is immutale means can't use add() remove().. etc

# from list 
# l=[1,25,6,69,54]
# fs=frozenset(l)
# print(fs)
# print(type(fs))

# from set
# s={12,58,98,65,36,1}
# fs=frozenset(s)
# print(fs)

# from range 
# fs=frozenset(range(10))
# print(fs)


# fs=frozenset(range(10))
# fs.add(586)
# print(fs)
# it will show an attribute error


# fs1=frozenset([12,556,85,69,36])
# fs2=frozenset([25,39,45,3,36])
# fs3=frozenset([6,2,32,33,31])

# fs1.add(25)1
# print(fs1)

# fs4=fs1.union(fs2)
# print(fs4)

# as like that everything like union intersection subset superset etc. will work with frozenset