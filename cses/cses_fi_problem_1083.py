n = int(input())
arr = map(int,input().split(' '))
print(int((n*(n+1))/2)-sum(arr))
