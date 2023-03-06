from sys import stdin, stdout
t=int(stdin.readline())
l=[map(int,stdin.readline().split()) for i in range(t)]
for i in range(N):
    y,x=l[i][0],l[i][1]
    n=max(x,y)
    print(n*n-n+1+((n%2)*2-1)*(x-y))
