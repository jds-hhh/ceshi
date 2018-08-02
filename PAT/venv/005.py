
class Student:
    def __init__(self,no,compsite):
        self.no=no
        self.compsite=compsite
    def __str__(self):
        return '{0} {1}'.format(self.no,self.compsite)

s={}
num=int(input())
for i in range(num):
    str = input()
    list1=str.split()
    s1=Student(list1[0],list1[2])
    s[list1[1]]=s1

num1=int(input())
str1=input()
list2=str1.split()

for i in range(0,num1):
    print(s.pop(list2[i]))



