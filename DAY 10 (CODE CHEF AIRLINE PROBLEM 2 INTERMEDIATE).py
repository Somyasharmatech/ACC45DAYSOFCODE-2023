# DAY 10 CODE CHEF AIRLINE PROBLEM 2 INTERMEDIATE.
# cook your dish here
for i in range(int(input())):
    A,B,C,D,E=map(int,input().split())
    if(A+B<=D) and (C<=E):
        print("Yes")
    elif(B+C<=D) and (A<=E):
        print("Yes")
    elif(A+C<=D) and (B<=E):
        print("Yes")
    else:
        print("No")
    