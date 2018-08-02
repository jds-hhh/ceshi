time=input().split(":")
hour=int(time[0])
minute=int(time[1])

if hour>12:
    if minute==0:
        for i in range(hour%12):
            print("Dang",end='')
    else:
        for i in range((hour%12)+1):
            print("Dang",end='')
else:
    print("Only {}:{}.  Too early to Dang.".format(time[0],time[1]))