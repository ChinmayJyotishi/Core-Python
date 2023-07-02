# WAP TO FIND OUT THE NUMBER OF OCCURENECES OF A CHARACTER PRESENT IN A STRING::


s="kaka"
# d={}

# for i in s:
#     d[i]=d.get(i,0)+1
# print(d)


s='chinmay jyotishi'
d={}
for i in s:
    d[i]=d.get(i,0)+1
print(d)

for i,j in d.items():
    print(f'{i} is present {j } times')





