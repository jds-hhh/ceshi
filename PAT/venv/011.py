str1=input()
str2=input()

result=[]
output=[0]*128
for i in str2:
    output[ord(i)]=i
for i in str1:
    if not i is output[ord(i)]:
        result.append(i)

for i in result:
    print(i,end='')