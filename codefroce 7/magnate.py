n = int(input())

magnets = [input() for i in range(n)]

groups = 1  # start with one group
for i in range(1, n):
    if magnets[i] != magnets[i-1]:
        groups += 1

print(groups)