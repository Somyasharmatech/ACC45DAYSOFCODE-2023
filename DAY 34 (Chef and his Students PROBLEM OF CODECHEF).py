# DAY 34 Chef and his Students PROBLEM OF CODECHEF
t=int(input())
while t!=0:
    s=str(input())
    count=0
    for i in range(len(s)-1):
        if s[i]=='<' and s[i+1]=='>':
            count+=1
    print(count)
    t-=1