# problem in the positional argument -- u have to pass in order
# 

def cal(a, b, c):
    print(a+b*c)

# cal(1,2,5)
# cal(5,2,1) #order changed value also changed
# cal(c=5,b=2,a=1)#order changed but value not changed

# you can use both positional and keyword argument at the same time but u have to remember on premium point


cal(5, 6, c=5)
cal(5, b=6, c=5)
# here it will through an error because u are passing more then one value of a
# cal(5, a=6, b=5)

# that premium point is that you can't write positional argumnet after keyword argument

# cal(5,b=6,5) #SyntaxError: positional argument follows keyword argument

# why we can't write like cal(5,b=6,5)


# def cal(a, b, c):
#     print(a+b*c)

# cal(5,a=2,5)
# here 5 goes to a then 2 also goes to a then whose value is 5 b or c, how will the complier know -thats why the error

# cal(5,b=2,5) now after writing this the issue must be solved but no again the same error why?

# ans --


# def cal( a,b, c, d, e,f):
#     print(a+b+c+d+e+f)


# call(2,3,4,e=4,10,15) #positional argument must be befor of keyword argument 
# cal(2,3,4,10,15,e=4) #multiple values error will occur

# ans is  actually the problem is not in the caller function the problem is in the called function
# 
# in caller function put the argument in last which keyword argument u are passing in the caller function

# def cal( a,b, c, d, f,e):
#     print(a+b+c+d+e+f)

# cal(2,3,4,10,15,e=4)



def add(a,b,c):
    print(a+b*c)


# add(10,20,30) #i have changed the order
# add(b=20,a=10,c=30)

# add(5,c=20,b=10)
# add(5,b=10,10)


def add(a,b,c,d,f,e):
    print(a+b+c+d+e+f)

add(10,20,5,2,55,e=10)