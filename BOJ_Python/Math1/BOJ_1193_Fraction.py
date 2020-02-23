x=int(input())

'''
n=1
#time over
if(x!=1):
    while 1:
        s=n*(n+1)//2
        if(s>x):
            break
        n=n+1
    #n짝수 -> 아래로, n홀수->위로
    last=s-n
    #print(last)
    if(n%2==0):
        down=n
        up=1
        dir=0
    else:
        up=n
        down=1
        dir=1

    while 1:
    #    print(x,last)
        last=last+1
        if(x==last):
            print("%d / %d"%(up,down))
            break
        if(dir):
            up=up-1
            down=down+1
    #        print(up,down)
        else:
            up=up+1
            down=down-1
    #        print(up,down)
elif (x==1):
    print(1)
'''

n=1
#time over
if(x!=1):
    while 1:
        s=n*(n+1)//2
        if(s>=x):
            break
        n=n+1
    #n짝수 -> 아래로, n홀수->위로
    last=s-n
    #print(last)

    if(n%2==0):
        down=n
        up=1
        dir=0
        print("%d/%d"%(up+(x-last-1),down-(x-last-1)))
    else:
        up=n
        down=1
        dir=1
        print("%d/%d"%(up-(x-last-1),down+(x-last-1)))
elif (x==1):
    print("1/1")
