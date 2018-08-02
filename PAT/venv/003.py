num=input()
list1=list(num)
number=[0,0,0,0,0,0,0,0,0,0]
for i in list1:
    number[int(i)]+=1
for i in range(10):
    if number[i]!=0:
        print(str(i)+':'+str(number[i]))