# DAY 29 Chef and Cook-Off
n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    if(l.count(1)==0):
        print("Beginner")
    elif(l.count(1)==1):
        print("Junior Developer")
    elif(l.count(1)==2):
        print("Middle Developer")
    elif(l.count(1)==3):
        print("Senior Developer")
    elif(l.count(1)==4):
        print("Hacker")
    elif(l.count(1)==5):
        print("Jeff Dean")