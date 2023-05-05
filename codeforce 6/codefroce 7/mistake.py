a = input()  # Read the first number
b = input()  # Read the second number

# Initialize an empty result string
result = ""

# Loop over the digits of the input numbers and compare them
for i in range(len(a)):
    if a[i] != b[i]:
        result += "1"  # Add a 1 if the digits differ
    else:
        result += "0"  # Add a 0 if the digits are the same

# Print the result
print(result)