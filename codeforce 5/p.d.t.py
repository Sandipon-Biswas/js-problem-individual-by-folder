input_str = input().lower()

vowels = "aeiouy"

result_str = ""

for char in input_str:
    if char in vowels:
        continue
    else:
        result_str += "." + char

print(result_str)