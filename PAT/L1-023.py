
table=[0]*128
table[ord('G')]=1
table[ord('P')]=1
table[ord('L')]=1
table[ord('T')]=1
str2=["G","P","L","T"]
str1=input()
sum=0
for i in str1:
    if table[ord(i.upper())]!=0:
        table[ord(i.upper())]+=1
        sum+=1
for i in range(sum):
    for j in range(4):
        if table[ord(str2[j])]!=1:
            print(str2[j],end='')
            table[ord(str2[j])]-=1
