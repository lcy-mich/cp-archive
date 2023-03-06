from sys import stdin, stdout

tests = [(int(stdin.readline()), list(map(int,stdin.readline().split()))) for i in range(int(stdin.readline()))]

for length, test in tests:
    two_pos = []
    for idx, element in enumerate(test):
        if element == 2:
            two_pos.append(idx+1)
    two_amount = len(two_pos)
    if two_amount == 0:
        stdout.write(f"1\n")
    elif two_amount % 2 == 0:
        position = two_pos[(two_amount//2)-1]
        stdout.write(f"{position}\n")
    else:
        stdout.write(f"-1\n")
