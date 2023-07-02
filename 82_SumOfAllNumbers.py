def sumofallnum(num):
    if num==1:
        return num
    return num+sumofallnum(num-1)
print(sumofallnum(3))