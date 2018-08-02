str=input()
list1=str.split()
a=int(list1[0])
b=int(list1[1])+1
sum=0
times=b-a
for i in range(1,times+1):
    if i%5!=0:
        print('{0:5}'.format(a),end='')
    else:
        print('{0:5}'.format(a),end='')
        print()
    sum+=a
    a+=1

if times%5!=0:
    print()
print("Sum = {}".format(sum))