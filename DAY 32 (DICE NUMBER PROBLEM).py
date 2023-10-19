# DAY 32 DICE NUMBER PROBLEM
T = int(input())
for i in range(T):
    res = list(map(int,input().split()))
    a= res[:3]
    b= res[3:]
    a.sort(reverse=True)
    b.sort(reverse=True)
    if a > b:
        print("Alice")
    elif a < b:
        print("Bob")
    else:
        print("Tie")