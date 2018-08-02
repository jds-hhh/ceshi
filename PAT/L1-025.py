import re
str1=input().split(' ',1)

a=str1[0]
b=str1[1]
if not a.isdigit() or not b.isdigit():
    if not a.isdigit():
        print("?",end=' + ')
    else:
        print(a,end=' + ')
    if not b.isdigit():
        print("? =",end=' ')
    else:
        print(b,end=' = ')
    print("?")
else:
    aint = int(a)
    bint = int(b)
    if aint>1000 or bint>1000 or aint<1 or bint<1:
        if aint>1000 or aint<1:
            print("?", end=' + ')
        else:
            print(a, end=' + ')
        if bint>1000 or bint<1:
            print("? =", end=' ')
        else:
            print(b, end=' = ')
        print("?")
    else:
        print("{} + {} = {}".format(aint,bint,aint+bint))