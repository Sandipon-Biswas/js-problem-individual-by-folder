s1, s2, s3, s4 = map(int, input().split())

unique_colors = set([s1, s2, s3, s4])
num_additional_horseshoes = 4 - len(unique_colors)

print(num_additional_horseshoes)