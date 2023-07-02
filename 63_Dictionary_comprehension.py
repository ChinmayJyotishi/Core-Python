# d={i:i for i in range(1,7)}
# print(d)


# d={i:i*i for i in range(1,7)}
# print(d)

# from list
l=[2.3,4.5,65.8,8.3]
d={i:3.14*i*i for i in l}
print(d)
print(type(d))


names=['chinmay','raja','mallik','kallu']
d={i:len(i) for i in names}
print(d)