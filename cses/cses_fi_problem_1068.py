
n = int(input())
arr = [str(n)]

while n>1:
    if n % 2 == 0:
        arr.append(str(n:=n//2))
    else:
        arr.append(str(n:=(n*3)+1))
        
print(" ".join(arr))
