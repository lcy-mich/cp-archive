dna = input()
longest = current = 1
past = ""
for base in dna:
    if past == base:
        current += 1
    else:
        current = 1
    longest = max(longest,current)
    past = base
print(longest)
