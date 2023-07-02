# find out the greates num
num=int(input("Enter ur 1st number\n"))
num1=int(input("Enter ur 2nd number\n"))
num2=int(input("Enter ur 3rd number\n"))

if num>num1 and num>num2:
    print(num," is greater")
elif num1>num2:
    print(num1,"  is greater")
else:
    print(num2," is greater")
