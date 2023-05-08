n = int(input())
feelings = ["I hate", "I love"]
result = "I hate"

for i in range(2, n+1):
    if i % 2 == 0:
        result += " that " + feelings[1]
    else:
        result += " that " + feelings[0]
    
result += " it"
print(result)