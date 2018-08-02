circlenum=int(input())

friends=[0]*1000000

for i in range(circlenum):
    str1=input().split()
    peoplenum=int(str1[0])
    for j in range(1,peoplenum+1):
        #记录该id是否在朋友圈里出现过
        if peoplenum>1:
            friends[int(str1[j])]+=1
searchnum=int(input())
searchpeople=input().split(" ")

handpeople=[]
for i in range(searchnum):
    if(friends[int(searchpeople[i])]==0):
        #将没有出现过的id记录到handpeople中
        handpeople.append(searchpeople[i])
        #防止重复输出
        friends[int(searchpeople[i])]+=1

if len(handpeople)==0:
    print("No one is handsome")
else:
    for i in range(len(handpeople)-1):
        print(handpeople[i],end=' ')
    print(handpeople[len(handpeople)-1])