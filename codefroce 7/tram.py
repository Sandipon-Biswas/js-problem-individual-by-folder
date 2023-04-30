x=int(input())
s=0
p=[]
for i in range(x):
    y,z=map(int,input().split())
    s=s-y+z
    p.append(s)
print(max(p))