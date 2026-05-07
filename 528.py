# def map_square(sequence):
#     new_lst = []
#     for n in sequence:
#         new_lst.append(n ** 2)

#     return new_lst
# print(map_square([-5, 0, 12, 2]))
def map_square(sequence):
    return map(lambda n : n ** 2, sequence)

print(list(map_square([-5, 2, 6])))