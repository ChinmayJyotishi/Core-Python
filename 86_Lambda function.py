#finding the sum of 2 numbers without using lambda function

def fun(a,b):
    return a+b
print(fun(10,20))

f=lambda a,b:a+b
print(f(10,20))

x=lambda n:n*n
print(x(10))


#find out the greatest number without usng lambda 

def greater(a,b):
    if a>b:
        return a
    else:
        return b
print(greater(25,889))
    
#find out the greatest number with usng lambda 
la=lambda a,b:a if a>b else b
print(la(895,25))


# lambda can return only one value 
# lm=lambda a,b:a,b #error 
# print(la(10,20))

lm=lambda a,b:a #no error 
print(la(10,20))


# lambda can return collections like tuple ,list

la=lambda a,b,c,d:[a,b,c,d]
print(la(10,20,58,64))


ml=lambda :"chinmay"
print(ml())

# find the greatest number in one line and without function name

print((lambda a,b: a if a>b else b)(10,20))