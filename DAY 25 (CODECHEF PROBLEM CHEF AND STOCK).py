# DAY 25 CODECHEF PROBLEM CHEF AND STOCKS
# cook your dish here
t=int(input())
while t>0:
    n=int(input())
    l=list(map(int,input().split()))
    n=100
    for i in l:
        if n>i:
            n=i
    l.remove(n)
    s=0
    for i in l:
        s+=i
    print(s)
    t-=1