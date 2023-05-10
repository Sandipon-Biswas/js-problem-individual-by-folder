n = int(input())
columns = list(map(int, input().split()))

# Sort the columns in ascending order
columns.sort()

# Print the sorted columns
print(*columns)