n = int(input())
stones = input()

count = 0
for i in range(1, n):
    if stones[i] == stones[i-1]:
        count += 1

print(count)