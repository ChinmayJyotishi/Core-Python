# calculator using python

from secrets import choice



while True:
    
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    operation=input("Operation::")
    if operation=='+':
        print("The + is",a+b)
        # break
    elif operation=='-':
        print("The - is",a-b)
        # break
    elif operation=='/':
        print("The / is",a/b)
        # break
    elif operation=='//':
        print("The // is",a//b)
        # break
    elif operation=='%':
        print("The '%' is",a%b)
        