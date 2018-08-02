str1=input().split(" ")

birth=str1[0]
n=int(str1[1])

count=0
year=int(birth)
a=[0]*4
b=[0]*10
while 1:
    a[0]=year//1000
    a[1]=year%1000//100
    a[2]=year%100//10
    a[3]=year%10
    for i in range(0,4):
        b[a[i]]+=1#对每一位计数
    for i in range(0,10):
        if b[i]:
            count+=1#计算0-9出现不重复的次数
    if count==n:
        break
    year+=1
    b=[0]*10
    count=0
year=str(year)
for i in range(4-len(year)):#将不足四位的年份补0
    year='0'+year
print(int(year)-int(str1[0]),year)