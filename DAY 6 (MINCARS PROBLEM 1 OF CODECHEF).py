#DAY 6 MINCARS PROBLEM 1 OF CODECHEF
for i in range(int(input())):
    x=int(input())
    c=x%4
    a=x//4
    if(x%4==0):
        print(a)
    if(x%4!=0):
        print(a+1)