n = int(input())  # number of rooms
count = 0  # count of available rooms

for i in range(n):
    p, q = map(int, input().split())
    if q - p >= 2:  # check if there's enough space for both George and Alex
        count += 1

print(count)