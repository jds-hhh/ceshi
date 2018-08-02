
result=[]
while 1:
    str=input()
    if str=='.':
        break
    else:
        result.append(str)

l=len(result)
if l<2:
    print("Momo... No one is for you ...")
if l<14 and l>1:
    print("{} is the only one for you...".format(result[1]))
if l>=14:
    print("{} and {} are inviting you to dinner...".format(result[1],result[13]))