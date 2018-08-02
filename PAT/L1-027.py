phonum=input()

arr=[]
index=[0]*11

for i in phonum:
    arr.append(i)
arr.sort()
arr.reverse()

arr1={}.fromkeys(arr).keys()
arr=list(arr1)
print("int[] arr = new int[]{",end='')
for i in range(len(arr)-1):
    print(arr[i],end=',')
print(arr[len(arr)-1],end='')
print("};")

print("int[] index = new int[]{",end='')
for i in range(len(phonum)-1):
    for j in range(len(arr)):
        if arr[j]==phonum[i]:
            print(j,end=',')
for j in range(len(arr)):
    if arr[j]==phonum[len(phonum)-1]:
        print(j,end='')
print("};",end='')

