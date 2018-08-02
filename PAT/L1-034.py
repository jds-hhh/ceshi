num=int(input())

tables=[0]*1001
for i in range(num):
    str1=input().split(" ")
    n=int(str1[0])
    for i in range(1,n+1):
        tables[int(str1[i])]+=1

max=1#记录编号最大的特性标签
n=0
for i in range(1,1001):
    if tables[i]>=n:
        max = i
        n=tables[i]

print(tables[max])
print(max,n)