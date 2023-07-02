# why default argument- because when we are passing less arguments it shows error 

# def fun(name):
#     print(f'hi {name} good morning')


# fun('chinmay')

# default argument
# def fun(name='unknown'):
#     print(f'hi {name} good morning')

# fun()
# fun('chinmay')


# # postional and default argument

# def msg(bf='u dont have bf', gf='u dont have gf'):
#     print(f'hi {bf}  {gf}')


# # msg('rahul', 'liza')
# msg('chinmay')
# msg('liza')
# msg(gf='liza')



def student(name,id,email='not available',mark):
    print('name is  ',name)
    print('id  is ',id)
    print('email  is ', email)
    print('mark  is ', mark)


student('chinmay',102423,55,665)

# here the error is because you have to write the default parameter at the end 

def student(name, id, mark, email='no'):
    print('name is  ', name)
    print('id  is ', id)
    print('email  is ', email)
    print('mark  is ', mark)


student('chinmay', 102423, 55)
