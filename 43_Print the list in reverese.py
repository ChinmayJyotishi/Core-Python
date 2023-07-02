# Printing the list in the reverse order with +ve index
l=[45,25,658,6,95]

# i=len(l)-1
# while i>=0:
#     print("{}   {}".format(l[i],  i))
#     i=i-1

# by -ve indexing
i=-1
while i>=-len(l):
    print(l[i])
    i=i-1