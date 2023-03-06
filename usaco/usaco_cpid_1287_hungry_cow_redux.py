from sys import stdin, stdout

n, t = map(int, stdin.readline().strip().split())
bales = []

total = 0
current = 0
next_i = 0

for day in range(1, t+1):
    if day-1 < n:
        bales.append(tuple(map(int, stdin.readline().split())))
    if next_i < n and bales[next_i][0] == day:
        current += bales[next_i][1]
        next_i += 1
    if current > 0:
        current -= 1
        total += 1

stdout.write(str(total))
