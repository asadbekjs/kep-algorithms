# Algorithm
# 1. max_1 ni topish
# 2. sonlarni ichidan max_1 o'chiramiz
# 3. qolgan sonlar ichidan max topish
def max_2(*args):
    max_1 = max(args)
    lst = list(args)
    lst.remove(max_1)
    return max(lst)

print(max_2(2, 3, 7, 5))
print(max_2(88, 9, 75, 56))