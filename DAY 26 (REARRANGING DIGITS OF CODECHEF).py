# DAY 26 REARRANGING DIGITS OF CODECHEF
t=int(input())
for i in range(0,t):
    d=int(input())
    n=input()
    if n[d-1]=="0" or n[d-1]=="5":
        print("YES")
    else:
        flag=0
        for j in n:
            if j=="0" or j=="5":
                flag+=1
        if flag>0:
            print("YES")
        else:
            print("NO")
            
        
    