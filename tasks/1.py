n = int(input()) # 4
lst = list(map(int, input().split())) # [12, 20, 99, 54] # range(4)
# s = 0
# for son in lst:
#     if son < 30 and son % 3 == 0:
#         print(son, end=" ")
#     else:
#         s += son # s = s + son

# print()
# print(s)
for index in range(len(lst)):
    print(index, lst[index])
