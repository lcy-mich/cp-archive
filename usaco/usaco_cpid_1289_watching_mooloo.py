from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
days = list(map(int, stdin.readline().split()))

cost = 0
last = days.pop(0)

for day in days:
    if day-last+k < 2+(2*k):
        cost += day-last+k+1
    else:
        cost += 2+(2*k)
    last = day   

stdout.write(str(cost))
