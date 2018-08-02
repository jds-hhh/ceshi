str1=input().split()
capA=int(str1[0])#A的酒量
capB=int(str1[1])#B的酒量
process=[]
num=int(input())#划拳的次数
for i in range(num):
    str2=input().split()
    process.append(str2)
for str2 in process:
    ha=int(str2[0])#A喊的数字
    hap=int(str2[1])#A划的数字
    hb = int(str2[2])  #B喊的数字
    hbp = int(str2[3])  #B划的数字
    sum=ha+hb
    if hap==sum and hbp!=sum:
        capA-=1#A输
        if capA<0:
            break
    if hbp==sum and hap!=sum:
        capB-=1#B输
        if capB<0:
            break

if capA<0:
    print("A")
    print(int(str1[1])-capB)
if capB<0:
    print("B")
    print(int(str1[0])-capA)