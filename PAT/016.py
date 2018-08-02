import math

class IDcheck:
    weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    check=['1','0','X','9','8','7','6','5','4','3','2']
    def __init__(self,no,verfiy):
        self.no=no
        self.verfiy=verfiy

    def checkNo(self):
        self.sum=0
        j=0
        for i in self.no:
            if ord(i)<48|ord(i)>57:#检验ASCII码是不是在0-9之间
                return False
            #计算权重
            self.sum=self.sum+self.weight[j]*int(i)
            j+=1
        self.sum=self.sum%11
        if self.check[self.sum]==self.verfiy:
            return True
        else:
            return False

    def __str__(self):
        return self.no+self.verfiy


n=int(input())
no=[]
ID=[]
for i in range(n):
    str1=input()
    ID.append(IDcheck(str1[0:17],str1[17]))

state=True
for i in range(ID.__len__()):
    if not ID[i].checkNo():
        state=False
        print(ID[i])

if state:
    print("All passed")

