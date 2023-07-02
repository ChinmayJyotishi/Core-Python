a=int(input("Enter ur 1st number\n"))
b=int(input("Enter ur 2nd number\n"))

ch=input("Enter ur choices like add/sub/mul/mod\n")

if ch=='add':
    print(a+b)
elif ch=="sub":
    print(a-b)
elif ch=="mul":
    print(a*b)
elif ch=="mod":
    print(a%b)

else:
    print("invalid option")
