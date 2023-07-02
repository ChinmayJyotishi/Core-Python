students={
    101:{'name':'chinmay','email':'chinmay@gmail.com','address':'Rairangpur'},
    102:{'name':'manoj','email':'manoj@gmail.com','address':'cuttack'},
    103:{'name':'rahul','email':'rahul@gmail.com','address':'bbsr'},
    104:{'name':'babu','email':'babu@gmail.com','address':'baripada'}
}

for k,v in students.items():
    print('student id is : ',k)

    for i in v:
        print(f'{i} is : {v[i]}')
    print('-'*20)