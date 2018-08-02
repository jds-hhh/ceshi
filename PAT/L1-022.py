num=int(input())
str1=input().split(" ")

odd=0
even=0
for i in str1:
    if int(i)%2==0:
        even+=1
    else:
        odd+=1
print(odd,even)
