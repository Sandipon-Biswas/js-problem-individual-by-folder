# x=int(input())
# num_str = str(x)
# is_lucky = True

# for digit in num_str:
#     if digit != '4' and digit != '7':
#         is_lucky = False
#         break
# if is_lucky == True :
#     print("YES")
# elif x%4==0 or x%7==0:
#     print("YES")
# else:
#     print("NO")
n = int(input())

# List of lucky numbers less than or equal to 1000
lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

# Check if n is almost lucky
if any(n % lucky_num == 0 for lucky_num in lucky_numbers):
    print("YES")
else:
    print("NO")