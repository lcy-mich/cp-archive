from sys import stdin, stdout
from random import choice

n = int(stdin.readline())
cows = list(stdin.readline().strip())
e = list(map(int, stdin.readline().split()))

count = 0

stdout.write(str(choice([1,2])))
