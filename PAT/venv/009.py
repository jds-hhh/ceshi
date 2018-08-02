import math

def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
class Factory:
    def __init__(self,mole,deno):
        self.mole=mole#分子
        self.deno=deno#分母

    def __add__(self, Factory):
        a=self.deno*Factory.deno;#分母
        b=self.mole*Factory.deno+self.deno*Factory.mole;#分子
        c=gcd(abs(a),abs(b))
        self.deno=a//c;
        self.mole=b//c;
        return self
    def __str__(self):

        if self.mole==0:
           return '0'
        string=''
        if self.mole*self.deno<0:
            string+='-'
        d=abs(self.deno)
        m=abs(self.mole)
        self.inte=m//d
        if self.inte>0:
            str1=str(self.inte)
            string+=str1
        m=m%d
        if m>0:
            if self.inte>0:
                string+=' '
            string+="{0}/{1}".format(m,d)
        return string

num=int(input())
str1=input()
list1=str1.split()
sum=Factory(0,1)
for i in range(num):
    list2=list1[i].split('/')
    a=int(list2[0])
    b=int(list2[1])
    f=Factory(a,b)
    sum=sum+f

print(sum)