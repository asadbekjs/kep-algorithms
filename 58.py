def filter_list(lst, a):
    new_lst = lst.copy()
    if a == 0:
        for number in new_lst:
            if number % 2 == 0:
                lst.remove(number)
        return lst
    else:
        for number in new_lst:
            if number % 2 == 1:
                lst.remove(number)
        return lst
    
print(filter_list([3, 5, 3, 6], 1))



