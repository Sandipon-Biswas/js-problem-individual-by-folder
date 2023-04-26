# x,y=map(int,input().split())
# z=[]
# for i in range(x+1):
#     if i%2 !=0:
#         z.append(i)
# for i in range(1,x+1):
#     if i%2 ==0:
#         z.append(i)      
# # print(z)
# print(z[y-1])
x, y = map(int, input().split())

if y <= (x+1)//2:
    # The number is in the odd part of the sequence
    print((y-1)*2+1)
else:
    # The number is in the even part of the sequence
    print((y-(x+1)//2)*2)