# DAY 38 PIZZA CUTTING 
m=int(input())
for _ in range(m):
    e=int(input())
    if(e%2==0 or e==1):
        print("YES")
    else:
        print("NO")