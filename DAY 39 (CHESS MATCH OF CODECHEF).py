# DAY 39 CHESS MATCH
for _ in range(int(input())):
    n,a,b = map(int, input().split())
    print((2*(180 + n)) - (a + b))