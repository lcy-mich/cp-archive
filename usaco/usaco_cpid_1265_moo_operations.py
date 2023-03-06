from sys import stdin, stdout

q = int(stdin.readline())

while q:
    q -= 1
    string = stdin.readline().strip()
    slen = len(string)
    if slen < 3:
        stdout.write("-1\n")
        continue
    if string == "MOO":
        stdout.write("0\n")
        continue
    if not string.find("MOO")+1:
        if not (string.find("MOM")+1 or string.find("OOO")+1):
            if not string.find("OOM")+1:
                stdout.write("-1\n")
                continue
            stdout.write(f"{str(slen-1)}\n")
            continue
        else:
            stdout.write(f"{str(slen-2)}\n")
            continue
    else:
        stdout.write(f"{str(slen-3)}\n")
    
        
    
    
