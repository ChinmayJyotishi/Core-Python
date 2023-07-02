num=int(input("pls enter a number\n"))
np=0
nn=0
nz=0
while num!=-1:
    if num>0:
        np=np+1
    elif num<0:
        nn=nn+1
    else:
        nz=nz+1
    num=int(input("pls enter a number\n"))
print("Number of +ve",np)
print("Number of -ve",nn)
print("Number of zero",nz)