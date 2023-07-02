l=[555,65,8,2,36,1]
min=l[0]
for i in l:
    if i<min:
        min=i
print(" min is",min)

l=[555,65,8,2,36,1]
max=l[0]
for i in l:
    if i>max:
        max=i
print(" max is",max)



l=[25,45,846,1,56]
min=l[0]
i=0
while (i<len(l)):
    if l[i]<min:
        min=l[i]
    i=i+1
print(min)