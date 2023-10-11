# DAY 24 CODECHEF PROBLEM
t=int(input())
for i in range (t):
    l,r,m=map(int,input().split())
    if m%l==0:
        p=m//l 
    else:
        p=((m//l)+1)
    q=m//r   
    print(p+q)