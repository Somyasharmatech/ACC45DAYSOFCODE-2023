# DAY 12 INTERMEDIATE CANDY PROBLEM BY CODECHEF
T=int(input())
for i in range(T):
    A,B=input().split()
    a=0 
    b=0 
    for i in range(1,1000):
        if i%2!=0:
            a=a+i
            if a>int(A):
                print("Bob")
                break
        else:
            b=b+i
            if b>int(B):
                print("Limak")
                break
            