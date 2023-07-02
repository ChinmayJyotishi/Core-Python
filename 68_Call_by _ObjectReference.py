# call by value -- if u do chnage in called function then it will not reflect to the outside of the function

# def fun(a):
#     print("inside function before modification",a)
#     print("inside function before modification",id(a))
#     a=1900
#     print("inside function after modification",a)
#     print("inside function after modification",id(a))


# a=15

# print("outside function before calling: ",a) 
# print("outside function before calling: ",id(a)) #554645889
# fun(a)
# print("outside function after calling: ",a)
# print("outside function after calling: ",id(a))


# call by referance--it means if u done any type of modification then it will reflect in the outside of the function

# def fun(l):
#     print("inside function before modification",l)
#     print("inside function before modification",id(l))
#     l.append(1500)
#     print("inside function after modification",l)
#     print("inside function after modification",id(l))



# l=[10,20,30]
# print("outside function before calling: ",l) 
# print("outside function before calling: ",id(l))
# fun(l)
# print("outside function after calling: ",l)
# print("outside function after calling: ",id(l))
# print(fun(l))