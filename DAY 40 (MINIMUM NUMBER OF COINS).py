# DAY 40 MINIMUM NUMBER OF COINS
for i in range(int(input())):
    x=int(input())
    if(x%10==0):
        print(x//10)
    elif(x%10!=0 and x%5==0):
        print((x//10)+1)
    else:
        print("-1")