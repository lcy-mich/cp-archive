from sys import stdin, stdout

N,T = tuple(map(int, stdin.readline().split()))
days = [0] * T

for i in range(N):
    day, bales = tuple(map(int, stdin.readline().split()))
    if day > T:
        break
    count = 0
    while bales:
        if day+count > T:
            break
        if days[day+count-1] == 0:
            days[day+count-1] = 1
            bales -= 1
        count += 1

ans = sum(days[:T])
stdout.write(str(ans))
