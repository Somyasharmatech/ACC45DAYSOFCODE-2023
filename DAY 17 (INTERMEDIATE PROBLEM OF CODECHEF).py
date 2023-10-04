# DAY 17 INTERMEDIATE PROBLEM OF CODECHEF
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    om=list(map(int,input().split()))
    andry=list(map(int,input().split()))
    oc=0
    ac=0
    occ=acc=0
    for i in range(n):
        if om[i]==0:
            oc=max(oc,occ)
            occ=0
        if om[i]!=0:
            occ+=1
        if andry[i]==0:
            ac=max(ac,acc)
            acc=0
        if andry[i]!=0:
            acc+=1
    oc=max(oc,occ)
    ac=max(ac,acc)
 
    if oc>ac:
        print('Om')
    elif ac>oc:
        print('Addy')
    else:
        print("Draw")