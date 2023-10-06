#DAY 19 INTERMEDIATE PROBLEM OF CODECHEF PRIME GENERATOR
import math as m
for _ in range (int(input())):
    m,n=map(int,input().split())
    x=dict()
    for i in range(2,int(n**(0.5)+1)):
        for j in range(max(2,m//i),(n//i)+1):
            x[i*j]=1
    for c in range(max(2,m),n+1):
        if c not in x:
            print(c)
    print()