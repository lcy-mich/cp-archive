from sys import stdin, stdout

t = int(stdin.readline())

tests = [(list(map(int, stdin.readline().split())), stdin.readline().replace('\n','')) for i in range(t)]

#(5 0) GHHGG

for i in tests:
    strlen, move, string = i[0][0], i[0][1], i[1]
    if move == 0:
        stdout.write(f"{strlen}\n{string}")
        continue
    if move >= strlen-1:
        stdout.write(f"2\nGH{'.'*strlen-2}")
        continue
    
