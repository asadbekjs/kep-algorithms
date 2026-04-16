# n = int(input())
# count = 0
# for son in range(1, n + 1):
#     if son % 12 == 0 or son % 5 == 0:
#         count += 1
# print(count)
# TL - Time Limited
# n // 5 + n // 12 - n // 60
# n = 60
# 60 // 5 = 12
# 60 // 12 = 5
# 60 // 60 = 1
# 12 + 5 = 17 - 1 = 16
n = int(input())
print(n // 5 + n // 12 - n // 60)