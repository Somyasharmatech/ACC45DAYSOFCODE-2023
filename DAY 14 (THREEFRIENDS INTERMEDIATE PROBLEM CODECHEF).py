#DAY 14 THREEFRIENDS INTERMEDIATE PROBLEM CODECHEF
T = int(input())

for i in range(T):
    X, Y, Z = list(map(int, input().split()))
    
    if (X + Y == Z) or (X + Z == Y) or (Y + Z == X):
        print('yes')
    else:
        print('no')