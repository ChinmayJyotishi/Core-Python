# a company decides to give bonus to his employee on this diwali
# a 5% bonus is given to male and 10% is given to female workers
# if the salary is less then 15000 then he or she will get 3% extra bonus

sal=int(input("enter ur salary\n"))
gen=input("enter ur gender\n")

if gen=='male':
    bonus=0.05*sal
elif gen=='female':
    bonus=0.10*sal
if sal<=15000:
    bonus=bonus+0.03*sal

sal=bonus+sal
if gen=='male':
    print("sir ur salary is",sal)
else:
    print('mam ur salary is ',sal)
