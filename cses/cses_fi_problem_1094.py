size, arr = int(input()), list(map(int, input().split(' ')))
minimum = 0

for i in range(size-1):
    if arr[i+1] < arr[i]:
        minimum += arr[i]-arr[i+1]
        arr[i+1] = arr[i]
print(minimum)
