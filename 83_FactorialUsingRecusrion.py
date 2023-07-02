# factorial of a number using recursion

def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)


print(fact(3))


def fact(n):
    if n<=1:
        return 1
    return n +fact(n-1)
print(fact(3))