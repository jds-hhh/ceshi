def isStandard(high,weight):
    w=(high-100)*0.9*2
    if abs(w-weight)<w*0.1:
        return 0#标准体重
    elif weight<w:
        return -1#太瘦
    if weight>w:
        return 1#太胖


num=int(input())
result=[]
for i in range(num):
    str1=input().split(" ")
    r=isStandard(int(str1[0]),int(str1[1]))
    if r==0:
        result.append("You are wan mei!")
    elif r==-1:
        result.append("You are tai shou le!")
    elif r==1:
        result.append("You are tai pang le!")

for i in result:
    print(i)