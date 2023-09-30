#DAY 13 ODDPAIRS INTERMEDIATE PROBLEM CODECHEF
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        e=n//2 - 1
        o=e +1
    else:    
        e=(n-1)//2
        o=(n+1)//2 -1
    
    if n%2 == 0:
        print((e*o)*2+(n))        
    if n%2 != 0:
        print((e*o)*2+(n-1))    