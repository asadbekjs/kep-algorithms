n = int(input())
i = 0
sonlar = []
while i < n:
    son = int(input())
    sonlar.append(son)
    i += 1

print(sonlar[-2], sonlar[-1])

# n = 5
# sikllar qadami:
# 1. 0 < 5 => True; son = 7; [7]; i = 1
# 2. 1 < 5 => True; son = 10; [7, 10]; i = 2
# 3. 2 < 5 => True; son = 4; [7, 10, 4]; i = 3
# 4. 3 < 5 => True; son = 108; [7, 10, 4, 108]; i = 4
# 5. 4 < 5 => True; son = 2; [7, 10, 4, 108, 2]; i = 5
# 5 < 5 => False; sikl tugaydi