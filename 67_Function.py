# def add(a,b,c):
#     print(a+b+c)


# add(10,55,60)


def add(a,b,c):
    '''this is a function which gives addition of 3 numbers'''
    print(a+b+c)
add(10,55,60)
print(add.__doc__)
print(min.__doc__)
# doc string--it is the description about your function and whenever u will hover on it it will describe u about that function

# def add(a, b, c):
#     print(a+b+c)


# add(10, 20, 30)
# add(11,12,13)


# def add(a, b, c):
#     print('Inside function')
#     print(id(a))
#     print(id(b))
#     print(id(c))
#     print(a, b, c)


# a, b, c = 10, 20, 30
# add(a, b, c)

# print('Outside function')
# print(id(a))
# print(id(b))
# print(id(c))
# print(a, b, c)


# def add(x, y, z):
#     print('Inside function')
#     print(id(x))
#     print(id(y))
#     print(id(z))
#     print(x, y, z)


# a, b, c = 10, 20, 30
# add(a, b, c)

# print('Outside function')
# print(id(a))
# print(id(b))
# print(id(c))
# print(a, b, c)


def add(x, y, z):
    print(id(x))
    x = 1008
    print('Inside function')
    print(id(x))
    print(id(y))
    print(id(z))
    print(x, y, z)


a, b, c = 10, 20, 30
add(a, b, c)

print('Outside function')
print(id(a))
print(id(b))
print(id(c))
print(a, b, c)