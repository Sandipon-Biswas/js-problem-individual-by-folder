s = input()

upper_count = 0
lower_count = 0

# Count the number of uppercase and lowercase letters in the word
for ch in s:
    if ch.isupper():
        upper_count += 1
    else:
        lower_count += 1

# Convert the word to all uppercase or all lowercase letters based on the count
if upper_count > lower_count:
    print(s.upper())
else:
    print(s.lower())