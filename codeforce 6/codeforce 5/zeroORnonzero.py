x = int(input())
sx = sy = sz = 0 # initialize the sums of forces in x, y, and z dimensions to zero
for i in range(x):
    a, b, c = map(int, input().split())
    sx += a # add the force component in x dimension
    sy += b # add the force component in y dimension
    sz += c # add the force component in z dimension

if sx == 0 and sy == 0 and sz == 0:
    print("YES")
else:
    print("NO")