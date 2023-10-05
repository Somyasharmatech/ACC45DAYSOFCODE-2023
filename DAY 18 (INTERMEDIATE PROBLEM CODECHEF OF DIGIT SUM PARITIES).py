#DAY 18 INTERMEDIATE PROBLEM CODECHEF OF DIGIT SUM PARITIES
for i in range(int(input())):
    n = int(input())
    copy = n
    su = sum([int(j) for j in str(n)])
    if su % 2 == 0:
        for k in range(copy+1, copy+5):
            t = sum([int(l) for l in str(k)])
            if t % 2 != 0:
                print(k)
                break
    elif su % 2 != 0:
        for k in range(copy+1, copy+5):
            t = sum([int(o) for o in str(k)])
            if t % 2 == 0:
                print(k)
                break