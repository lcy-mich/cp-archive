from sys import stdin, stdout

n = int(stdin.readline())
cows = stdin.readline().strip()
e = list(map(int, stdin.readline().split()))

leaders = {"H" : [], "G" : []}

enumeratedcows = enumerate(cows)

swap = lambda x : "H" if x == "G" else "G"
change1 = lambda x : 1 if x > 0 else 0

for i,cow in enumeratedcows:    
    if cows[i : e[i]].count(cow) == cows.count(cow):
        leaders[cow].append(i)
for i,cow in enumeratedcows:
    for j in leaders[swap(cow)]:
        if i >= j >= e[i]:
            leaders[cow].append(i)



stdout.write(str(max(leaders["H"], leaders["G"])[0]))
            
