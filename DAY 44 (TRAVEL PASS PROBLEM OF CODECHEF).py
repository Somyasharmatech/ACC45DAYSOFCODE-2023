# DAY 44 TRAVEL PASS PROBLEM OF CODECHEF
t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    s=input()
    x=0
    y=0
    for i in s:
        if(i=="0"):
            x=x+a 
        else:
            y=y+b  
    print(x+y)