def fun(**a):
    print(a)


# fun(10, 20)  # TypeError: fun() takes 0 positional arguments but 2 were given

# fun(a=10, b=20)  # no error
# fun(a=10, b=20, z=[10, 0, 20])


# def fun(**args, x):
#     print(a)
#     print(x)


# fun(a=10, b=20)

# def fun(x, **args):
#     print(a)
#     print(x)

# fun(a=10, b=20)# 1 error that is missing value of x
# fun(a=10, b=20, x=20)

# def fun(x, *b, **a):
#     print(x)
#     print(b)
#     print(a)


# fun(10, a=20, b=30)
# fun(10, 20, 66, a=28)


# def fun(x, **a, *b):  # syntax error
#     print(x)
#     print(b)
#     print(a)


# # variable length keyword argument should be after non keyword argument
# fun(10, 20, 66, a=28)


# def fun(**a):
#     print(a)

# fun()
# fun(a={})
