from sys import stdin, stdout

def takelast(elem):
    return elem[-1]

n,m = tuple(map(int,stdin.readline().split()))
cows = [list(map(int,stdin.readline().split())) for i in range(n)]
ac = [list(map(int,stdin.readline().split())) for i in range(m)]


stalls = [0 for i in range(100)]

for i in range(n):
    for j in range(cows[i][0],cows[i][1]+1):  
        stalls[j] = cows[i][2]

ac.sort(key=takelast)
total = 0
count = 0
while True:
    for i in range(ac[count][0],ac[count][1]+1):
        stalls[i] -= ac[count][2]
    total += ac[count][3]
    count += 1
    canbreak = True
    for i in stalls:
        if i > 0:
            canbreak = False
    if canbreak:
        break

stdout.write(str(total))

