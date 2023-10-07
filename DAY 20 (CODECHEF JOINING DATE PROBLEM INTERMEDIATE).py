# DAY 20 CODECHEF JOINING DATE PROBLEM INTERMEDIATE
T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    def func(n):
        return n*5
    if n%5 == 0:
      divs = [i for i in range(1,(n//5)+1)]
      divs = list(map(func, divs))
    else:
      divs = [i for i in range(1,(n//5)+2)]
      divs = list(map(func, divs))
    count = 1
    for i in divs:
      if i < k:
        count += 1
      else:
        break
    print(len(divs[count:]))