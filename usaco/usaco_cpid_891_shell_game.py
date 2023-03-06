#usacp cpid 891 shell game

import sys

sys.stdin = open('shell.in', 'r')
sys.stdout = open('shell.out', 'w')

n = int(input())

shell = [0,1,2]
count = [0,0,0]

def dangbro(s):
    return int(s)-1

for i in range(n):
    a,b,g = map(dangbro, input().split())

    shell[a], shell[b] = shell[b], shell[a]

    count[shell[g]] += 1

print(max(count))
