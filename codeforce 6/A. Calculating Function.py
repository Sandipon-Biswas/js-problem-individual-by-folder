# y=int(input())
# x=0
# for i in range(y+1):
#     if i%2 !=0:
#         x=x-i
#     else:
#         x=x+i
# print(x)
n = int(input())

if n % 2 == 0:
    # If n is even, f(n) = n / 2
    print(n // 2)
else:
    # If n is odd, f(n) = -(n+1) / 2
    print(-(n+1) // 2)