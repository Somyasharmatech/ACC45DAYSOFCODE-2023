#DAY 36 CRICKET RATING PROBLEM OF CODECHEF
t=int(input())
while(t):
    p1=list(map(int,input().split()))
    p2=list(map(int,input().split()))
    c1=0
    c2=0
    for i in range(3):
        if(p1[i]>p2[i]):
            c1=c1+1
        else:
            c2=c2+1
    if(c1>c2):
        print("A")
    else:
        print("B")
    t=t-1
    