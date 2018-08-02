
def getValuesPrint(a,b):
    if b==0:
        return str(a)+'/'+str(b)+'='+'Error'
    values=a/b
    str2=str(a)+'/'
    if b<0:
        str2=str2+'('+str(b)+')'
    else:
        str2=str2+str(b)
    str2=str2+'='

    return str2+str(format(values,'.2f'))

str1=input().split(" ")

a=int(str1[0])
b=int(str1[1])

print(getValuesPrint(a,b))
