import sys

ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abc = {i : 0 for i in ab}

sys.stdin = open("blocks.in","r")
sys.stdout = open("blocks.out","w")

n = int(input())

words = []
for i in range(n):
    word1,word2 = input().split()
    for i in ab:
        abc[i] += max(word1.count(i), word2.count(i))

for i in abc.values():
    print(i)
