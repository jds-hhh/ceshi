import math
num=int(input())

str1=input()
str1=list(str1)
ch=[None]*2000

length=len(str1)

for i in range(length):
    ch[i]=str1[i]

if length%num:#有余数，打印空格部分
        for i in range(length,(length//num+1)*num):
            ch[i]=' '
        length=length//num
else:
    length=length//num-1

for i in range(num):
    for j in range(length,-1,-1):
        print(ch[j*num+i],end='')
    print()