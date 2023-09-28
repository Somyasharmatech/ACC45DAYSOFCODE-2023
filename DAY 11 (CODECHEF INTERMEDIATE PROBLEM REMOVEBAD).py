# DAY 11 CODECHEF INTERMEDIATE PROBLEM REMOVEBAD
t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    b=0
    m=1
    a=l[0]
    i=1
    while(i<n):
        if(l[i]==a):
            i+=1
            m+=1
        else:
            a=l[i]
            i+=1
            if(m>b):
                b=m
            m=1
    if(m>b):
            b=m
    print(n-b)