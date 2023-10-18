#DAY 31 PROBLEM NO TIME TO WAIT OF CODECHEF
N, H, x = map(int, input().split())
T = list(map(int, input().split()))

if any(T[i] + x == H for i in range(N)):
    print("YES")
else:
    print("NO")