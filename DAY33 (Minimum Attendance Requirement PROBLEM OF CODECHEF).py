# DAY33 Minimum Attendance Requirement PROBLEM OF CODECHEF
for _ in range(int(input())):
    n=int(input())
    b=input()
    m= b.count('1')
    p=((m+(120-n))/120)*100
    if p>=75:
        print("YES")
    else:
        print("NO")