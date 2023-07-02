# myinfo={
#     'name':"wakir hussen",
#     'email':"wakirhussen10@gmail.com",
#     'mobile':"651454418463698",
#     'address':"Out of the earth",
# }
# print(myinfo)
# print(myinfo['name'])

# dictionary keys are case sensitive means if u r giving the keys as same name then it will update the value
# myinfo={
#     'name':"wakir hussen",
#     'name':"chinlknviusgv",
#     'email':"wakirhussen10@gmail.com",
#     'mobile':"651454418463698",
#     'address':"Out of the earth",
# }
# print(myinfo)


# creation of dictionary in many ways::

# creating an empty dictionary 
# d={}
# print(d)

# assign the values in an empty dictionary::
# d={}
# # d['name']='chinmay'
# d['course']='b.tech'
# d['sec']='A'

# print(d)

# creating a dictionary directly 


# myinfo={
#     'name':"wakir hussen",
#     'name':"chinlknviusgv",
#     'email':"wakirhussen10@gmail.com",
#     'mobile':"651454418463698",
#     'address':"Out of the earth",
# }
# print(myinfo)


# by using dict() method
# d=dict({'name':'chinmay'})
# print(d)


# d={
#     1:'aloo',
#     2:'bhindi',
#     3:'tomato',
# }
# print(d[1])
# print(d[0])  #it will give a key error as the given key is not present 


# check wheather the key is present or not
# by using has_key() method

# d={
#     1:'aloo',2:'bhindi',3:'tomato',
# }
# print(d.has_key(2))
# has_key() method is not supporeted by python3 it is supported  by python2

# as a solution of this u can use in operator

# print(2 in d)
# print(5 not in d)
# print(2 not in d)


# creating a  dictionary by user input

# d={}
# while True:
#     key=input("Enter your key : ")
#     val=input("Enter your value : ")

#     d[key]=val

#     choice=input("Do you want to add more elements [Y/N]: ").upper()

#     if choice=='N'or 'n':
#         break
# print(d)

# for the solution of n you can use or operator in if or you can make lower case to upper case by using upper()


# Traversing the dictionary 

# student={1:'chinmay',2:'raja',3:'manoj'}

# for i in student:
#     print(i,student[i])

# modification in dictionary 

# add
# cars={1:'bmw',2:'audi',3:'tata',4:'mahindra'}
# print(cars)
# cars[5]='toyota'
# print(cars)


# MODIFY
# cars={1:'bmw',2:'audi',3:'tata',4:'mahindra'}
# print(cars)
# cars[1]='toyota'
# print(cars)
 
# DELETE
# cars={1:'bmw',2:'audi',3:'tata',4:'mahindra'}
# print(cars)
# del cars[4]
# print(cars)
# if the key is not available means keyerror

# how to delete entire dicionary
# cars={1:'bmw',2:'audi',3:'tata',4:'mahindra'}
# print(cars)
# del cars
# print(cars)

# d = {[21, 22, 23]: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)


# d = {(21, 22, 23): 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)


# l = [21, 22, 23]
# d = {l: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)

# l.append(100)


# s = set((10, 20, 30))
# d = {s: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)


# s = set((10, 20, 30))
# d = {frozenset(s): 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)

# s = set((10, 20, 30))
# d = {frozenset(s): 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d[frozenset({10, 20, 30})])

# d = {12+13j: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)


# d = {True: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)

# d = {{1: 'one'}: 'surendra', 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)


# d = {23: {1: 'one'}, 24: 'priyanka', 25: 'rahul', 26: 'zini'}
# print(d)





students={
    1:{
        'name':'javed',
        'age':21,
        'branch':'cse',
        'grade':{
            '10th':85,
            '12th':65,
            'btech':85
        }
    }
}
# print(students,end=' ')

for i in students.keys():
    for j in students[i]:

        print(j,students[i][j])