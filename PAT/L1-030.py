num=int(input())

boys={}
girls={}

for i in range(num):
    people=input().split(' ')
    sex=people[0]
    if sex=='0':
        girls[i]=people[1]
    else:
        boys[i]=people[1]

girlskey=list(girls.keys())
boyskey=list(boys.keys())
girlsvalue=list(girls.values())
boysvalue=list(boys.values())
j=0
k=0
for i in range(int(num/2)):
    #女孩的排名比男孩的高，则拿出女孩第一名和男孩最后一名
    if girlskey[k]<boyskey[j]:
        print("{} {}".format(girlsvalue[k],boysvalue[int(num/2)-k-1]))
        k+=1
    else:
        print("{} {}".format(boysvalue[j],girlsvalue[int(num/2)-j-1]))
        j+=1