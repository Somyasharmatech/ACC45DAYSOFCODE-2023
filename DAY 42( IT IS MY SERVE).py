# DAY 42 IT IS MY SERVE
serve = int(input())
for s in range(serve):
  a,b=map(int,input().split())
  print("alice") if (a+b)%4==0 or (a+b)%4==1 else print("bob")