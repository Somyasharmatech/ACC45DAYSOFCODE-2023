# DAY 37 CHANGE IT PROBLEM OF CODECHEF
for i in range(int(input())):
    n=int(input())
    d=dict()
    l=sorted(list(map(int,input().split())))
    for i in range(len(l)):
        k=1
        for j in range(i+1,len(l)):
            if(l[i]==l[j]):
                k=k+1
        if(l[i] not in d):
            d[l[i]]=k
    print(n-max(d.values()))