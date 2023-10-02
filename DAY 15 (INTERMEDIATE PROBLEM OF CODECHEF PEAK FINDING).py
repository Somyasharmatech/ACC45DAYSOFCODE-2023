# DAY 15 INTERMEDIATE PROBLEM OF CODECHEF PEAK FINDING
T=int(input())
while(T):
    x=[]
    N=int(input())
    for i in range (0,N):
        num=int(input())
        x.append(num)
    max=0
    for j in range (0,N):
        if(x[j] >=max):
            max=x[j]
    print('{}\n'.format(max))
    T=T-1