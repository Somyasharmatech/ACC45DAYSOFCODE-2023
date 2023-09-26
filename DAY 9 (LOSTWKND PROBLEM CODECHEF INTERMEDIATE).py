# DAY 9 LOSTWKND PROBLEM CODECHEF INTERMEDIATE
T=int(input())
for i in range(T):
    a1,a2,a3,a4,a5,p=map(int,input().split())
    n = (a1 + a2 + a3 + a4 + a5) * p
    if n > 120:
        print("Yes")
    else:
        print("No")