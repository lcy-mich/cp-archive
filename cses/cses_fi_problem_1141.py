from sys import stdin, stdout
def main():
    length = int(stdin.readline())
    arr = map(int,stdin.readline().split())

    longsubarr = []
    index = dict(zip(arr,[0 for i in range(length)]))
    long = 0
    print(index)
    for songid in arr:
        if songid in longsubarr:
            break
        longsubarr.append(songid)
        long = max(long, len(longsubarr))
    stdout.write(str(long))
    return

if __name__ == "__main__":
    main()
        
        
