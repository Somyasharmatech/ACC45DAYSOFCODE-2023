#DAY 23 CODECHEF NON NEGATIVE PRODUCT 
# cook your dish here
for _ in range(int(input())):
    n =  int(input())
    a = list(map(int, input().split()))
    cout=1
    for i in a:
        cout*=i
    if cout<0:
        print(1)
    elif cout==0:
        print(0)
    else:
        print(0)