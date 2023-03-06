import sys

sys.stdin = open('speeding.in','r')
sys.stdout = open('speeding.out','w')

n,m = map(int,input().split())
road = []
for i in range(n):
    l,r = list(map(int,input().split()))
    road.extend([r]*l)
journey = []
for i in range(m):
    l,r = list(map(int,input().split()))
    journey.extend([r]*l)
largest = 0
for i in range(100):
    largest = max(largest, (journey[i]-road[i]))
print(largest)
