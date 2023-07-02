# SPLIT()::

s="chinmay jyotishi"
print(s.split())
# split function is used to separate the string 
# if u are not passsing any argument then in the place of space in string it will split the string and separate the words

# s="chinmay jyotishi"
# print(s.split('i'))
# it will separate the string where the 'i' is present

# s="chinmay jyotishi"
# print(s.split('h'))

# JOIN()::

l=['chinmay',' is',' a very ','good boy']
# s='+'.join(l)
# print(s)
s=''.join(l)
print(s)
s='-'.join(l)
print(s)


# l=('chinmay',' is',' a very ','good boy')
#  s='+'.join(l)
# print(s)
# s=''.join(l)
# print(s)
# s='-'.join(l)
# print(s)

# STRIP(),LSTRIP(),RSTRIP()
# it is used to remove the space from

# RSTRIP
# IT IS USED TO REMOVE THE SPACE FROM RIGHT SIDE
# s="chinmay     "
# print(len(s))
# print(s)
# print(s.rstrip())
# print(len(s.rstrip()))

# LSTRIP
# IT IS USED TO REMOVE THE SPACE FROM LEFT SIDE
# s="     chinmay"
# print(len(s))
# print(s)
# print(s.lstrip())
# print(s)
# print(len(s.lstrip()))

# STRIP()
# REMOVE THE SPACE FROM BOTH SIDE 

# s="     chinmay         "
# print(len(s))
# print(s)
# print(s.strip())
# print(len(s.strip()))


# zfill()::
# s="chinmay"
# print(len(s))
# print(s.zfill(15))
# yahan pe chinmay main total character 7 hai lekin mene zfill main 15 pass kiya hai so ye kya karega ki chinmay ko 15 character banane ke kosis karega 
# kaise-- name se pehele rest zero add karke

# # RJUST()::
s="chinmay"
print(s.rjust(10))

# it will first print in right side then add space in left and you can change default value to * - / any thing

# s="chinmay"
# print(s.rjust(10, '*'))

# lJUST()::
# s="chinmay"
# print(s.ljust(10))
# it will first print in left side then add space in right and you can change default value to * - / any thing
# s="chinmay"
# print(s.ljust(10,'*'))

# CENTER()::
# s='chinmay'
# print(s.center())
# print(s.center(20,'*'))
# it will first print the string in center then add rest space or character to make the complete size what u have passed in argument

# min()
# s='chinmay'
# print(min(s))

# max()
# s='chinmay'
# print(max(s))

# sorted()


# s='chinmay'
# print(sorted(s))
# it will print in ascending order and in the form of list 

# s='chinmay'
# print(sorted(s,reverse=True))
# for descending order

# isidentifier():
# it will check that is your string an identifier or not 
# s='123absc'
# print(s.isidentifier())
# s='absc123'
# print(s.isidentifier())
# s='*absc123'
# print(s.isidentifier())


# s="chinmay"

# for i in enumerate(s):
    # print(i)

# for i,j in enumerate(s):
#     print(i,j)