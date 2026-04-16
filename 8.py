# 1030800 => 2
n = int(input())
count = 0
# print(str(n)[::-1]) # 0080301
for digit in str(n)[::-1]:
    if digit == '0':
        count += 1
    else:
        break

print(count)