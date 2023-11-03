# DAY 44 CHEF AND STRINGS
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    
    for i in range(n-1):
        cnt += (abs(a[i+1] - a[i])-1)
    print(cnt)
        
    