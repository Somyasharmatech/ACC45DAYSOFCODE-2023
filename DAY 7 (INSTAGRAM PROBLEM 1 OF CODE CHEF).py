#DAY 7 INSTAGRAM PROBLEM 1 OF CODE CHEF
v=int(input())
for _ in range(v):
    a,b=list(map(int,input().split()))
    if a>10*b:
        print("YES")
    else:
        print("NO")