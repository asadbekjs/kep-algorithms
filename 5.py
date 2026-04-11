# 1 + 2 + 3 + ... + (n - 1) + n
# n = int(input())
# s = 0
# for son in range(1, n + 1):
#     s += son # s = s + son

# print(s)
# n = 4
# Sikllar qadami:
# 1. son = 1; s = 0 + 1 = 1
# 2. son = 2; s = 1 + 2 = 3
# 3. son = 3; s = 3 + 3 = 6
# 4. son = 4; s = 6 + 4 = 10
# Natija: s = 10

import math
# print(int(math.sqrt(8)))
# print(int(math.sqrt(9)))
n = int(input())
s = 0
for son in range(1,n + 1):
    s += int(math.sqrt(son))
print(s)
