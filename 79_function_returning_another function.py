# # Function returning another function ex 1
# def outer():
#     print('hello outer')

#     def inner():
#         print('hello inner')
#     print('..........')
#     return inner


# x = outer()
# x()
# x()
# x()

def fun1(abc):
    print('abc id is :', id(abc))
    return abc


def x():
    print('x id is ', id(x))
    print('python....')


data = fun1(x)
print('data id is ', id(data))
data()




# def outer(abc):
#     return abc

# def x():
#     print('python')
# c=outer(x)
# c()
