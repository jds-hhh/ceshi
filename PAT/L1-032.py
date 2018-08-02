str1=input().split(" ")
num=int(str1[0])
sign=str1[1]

str2=input()
l=len(str2)

d=num-l
r=''
if d==0:
    print(str2)
if d>0:
    for i in range(abs(d)):
        r+=sign
    str2=r+str2
    print(str2)
if d<0:
    print(str2[l-num:l])