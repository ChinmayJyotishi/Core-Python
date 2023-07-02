# wap to take bf n gf as input and make a dictionary then type bf name to get gf name
from secrets import choice


d={}
while True:
    bf=input("Enter the bf name: ")
    gf=input("Enter the gf name: ")
    d[bf]=gf

    choice=input("Do you want to add more [Y/N]").upper()

    if choice=='N':
        break
    
while True:
    bf=input("Enter the bf name to know gf name:: ")
    gf=d.get(bf)
    print(f'Hi {bf} your gf name is {gf}')
    
    choice=input("Do you want to search more [Y/N]").upper()

    if choice=='N':
        break
