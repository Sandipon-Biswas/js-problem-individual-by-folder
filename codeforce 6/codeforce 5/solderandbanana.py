k, n, w = map(int, input().split())
a, b, c= input().split()
a = int(a)
b = int(b)
c = int(c)
array=[]
for i in range(1,c+1):
    v=a*i
    array.append(v)
r=sum(array)
if(r>b):
    f=r-b
else:
    f=0

print(f)