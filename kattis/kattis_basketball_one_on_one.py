a = 0
b = 0
s = list(input())
while s:
    if s.pop(0) == "A":
        a += int(s.pop(0))
    else:
        b += int(s.pop(0))
if a > b:
    print("A")
else:
    print("B")
