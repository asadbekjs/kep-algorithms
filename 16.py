n = int(input())
s = 1
for son in range(1, n + 1):
    s *= son

print(s)
# n = 4
# sikldagi qadamlar:
# 1. son = 1 --> s * 1 = 1
# 2. son = 2 --> s * 1 = 1 * 2 = 2
# 3. son = 3 --> s * 3 = 2 * 3 = 6
# 4. son = 4 --> s * 4 = 6 * 4 = 24
