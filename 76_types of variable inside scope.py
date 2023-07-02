# def fun():
#     a=20 #local variable
#     print(a)


# def fun1():
#     print(a)

# fun()
# fun1()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# global variable 

# a=99

# def fun():
#     print(a)
# fun()


# def fun1():
#     print(a)
# fun1()

# a=65

# def fun():
#     a=98
#     print(a)

# fun()

# def fun1():
#     print(a)
# fun1()


# global function

a=23

def fun():
    a=99
    print(a)
    # print(globals()['a'])
    data=globals()['a']
    print(data)

fun()



    