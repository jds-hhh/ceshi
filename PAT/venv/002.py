import math
str=input().split(' ')
num=int(str[0])
sign=str[1]
num1=int(math.sqrt((num+1)/2))

for i in range(0,num1):#打印沙漏的上半部分
    for k in range(i):
        print(' ', end='')
    for j in range(0,2*(num1-i)-1):
        print(sign,end='')
    print()
for i in range(1,num1):#打印沙漏的下半部分
    for k in range(num1-i-1):
        print(' ', end='')
    for j in range(0,2*i+1):
        print(sign,end='')
    print()
d=num-2*num1*num1+1
print(d,end='')