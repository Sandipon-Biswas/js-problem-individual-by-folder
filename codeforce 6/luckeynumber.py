n = input().strip()
s=0
for i in n:
    if i=="7" or i=="4":
        s+=1
if s==7 or s==4:
    print("YES")
else:
    print("NO")