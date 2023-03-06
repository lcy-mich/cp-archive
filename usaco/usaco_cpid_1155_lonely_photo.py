from sys import stdin, stdout

n = int(stdin.readline())
string = list(stdin.readline().replace('\n',''))
last3 = []
remove = 0

for char in string:
    last3.append(char)
    if len(last3) >= 3:
        if last3.count("G") == 1:
            remove +=1
        if last3.count("H") == 1:
            remove += 1
        last3.pop(0)
stdout.write(str(remove))
