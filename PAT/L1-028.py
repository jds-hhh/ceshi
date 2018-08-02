from math import sqrt
def isPrimeNum(number):
    if number<2:
        return True
    a=2
    b=int(sqrt(number))+1
    while a<b:
        if number%a==0:
            return False
        a+=1
    return True

num=int(input())
num1=[]
for i in range(num):
    num1.append(input())

for i in num1:
    if isPrimeNum(int(i)):
        print("Yes")
    else:
        print("No")

