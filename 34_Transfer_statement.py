# pass continue break
# for i in range(10):
#     print(i)          #after printing the 6 it will be stopped
#     if i==6:
#         break

# for i in range(10):
#     if i==6:
#         break
#     print(i)          #before printing the 6 it will be stopped

# COTINUE MEANS SKIP
# for i in range(10):
#       if i==4:
#         continue
#       print(i)

# for i in range(10):
#       if i==4  or i==6:
#         continue
#       print(i)


# PASS MEANS IT GIVE EMPTY VALUE 
for i in range(10):
    if i%2==0:
        pass             
    else:
        print(i)
