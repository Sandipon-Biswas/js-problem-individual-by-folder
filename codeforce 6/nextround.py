n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Count the number of participants who earned a score equal to or greater than the k-th place finisher's score
count = 0
for score in scores:
    if score >= scores[k-1] and score > 0:
        count += 1
    else:
        break

print(count)