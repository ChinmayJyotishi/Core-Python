def calculations_at_own(a, b):
    print(a, b)

# calculations_at_own(10,25)
cal=calculations_at_own
cal(55,66)
del calculations_at_own
cal(6655)
# calculations_at_own(2889,897) #you cant call because this name is already deleted .you will get error
