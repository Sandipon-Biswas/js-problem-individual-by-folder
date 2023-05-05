x= int(input())
s = sorted(list(map(int, input().split())))
n = 1 
while sum(s[-n:]) <= sum(s[:len(s)-n]):
    n += 1
print(n)