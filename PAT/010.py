def swaps(a,b):
    return b,a

def main():
    str=input()
    list1=str.split()
    a=int(list1[0])
    b=int(list1[1])
    c=int(list1[2])
    if(a>b):
        a,b=swaps(a,b)
    if(b>c):
        b,c=swaps(b,c)
    if(a>b):
        a,b=swaps(a,b)
    print('{}->{}->{}'.format(a,b,c))
if __name__ == "__main__":main()