def sum_of_digits(number):
    s = 0
    for char in str(number):
        digit = int(char)
        s += digit

    return s
# print(sum_of_digits(152)) # 8 

for son in range(1000, 10000):
    if sum_of_digits(son) % 2 == 0:
        print(son, end=" ")