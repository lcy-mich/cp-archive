import sys

sys.stdin = open("cowsignal.in","r")
sys.stdout = open("cowsignal.out","w")

m,n,k = map(int, input().split())
lines = [input() for i in range(m)]

for i in range(m):
    current = ''
    for j in lines[i]:
        current += j*k

    for j in range(k):
        print(current)
    
