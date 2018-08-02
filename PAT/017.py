str=input()
num=int(str)
percentage=1
numSecond=0

for i in str:
    if i=='2':
        numSecond+=1

if num<0:
    percentage=numSecond/(len(str)-1)*1.5
else:
    percentage=numSecond/(len(str))
if num%2==0:
    percentage=percentage*2

percentage=percentage*100
print(format(percentage,'.2f')+"%")