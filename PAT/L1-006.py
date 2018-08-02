from math import sqrt
num=int(input())
lim=int(sqrt(num))

max_length=0
max_start=0
for i in range(2,lim+2):
    if num%i==0:#找到第一个被整除的数
        start=i
        j=i
        length=0
        n=num
        while n%j==0:
            n/=j
            j+=1
            length+=1
        #找到更长的连续因子
        if length>max_length:
            max_length=length
            max_start=start

#素数
if max_length==0:
    max_start=num
    max_length=1

print(max_length)
for i in range(max_start,max_start+max_length-1):
    print(str(i),end='*')

print(str(max_start+max_length-1))