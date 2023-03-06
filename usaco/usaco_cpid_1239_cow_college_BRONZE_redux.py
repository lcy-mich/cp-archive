from sys import stdin, stdout

n = int(stdin.readline())
tuition = list(map(int, stdin.readline().split()))

mean = round(sum(tuition)/n)
amount = 0

for i in tuition:
    if mean <= i:
        amount += 1

stdout.write(f"{mean*amount} {mean}")
