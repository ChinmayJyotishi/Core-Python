a=10
a=[1,2,3,4,5]
sum=0

for ele in a:
    sum+=ele
print(sum)

count=0
while(True):
    if count%3==0:
        print(count, end=" ")
    if(count>15):
        break;
    count+=1