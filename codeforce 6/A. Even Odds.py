x,y=map(int,input().split())
z=[]
for i in range(x+1):
    if i%2 !=0:
        z.append(i)
for i in range(1,x+1):
    if i%2 ==0:
        z.append(i)      
# print(z)
print(z[y-1])