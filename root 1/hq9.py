program = input().strip()

found_output = False
for c in program:
    if c == 'H' or c == 'Q' or c == '9':
        found_output = True
        break
if found_output:
    print("YES")
else:
    print("NO")