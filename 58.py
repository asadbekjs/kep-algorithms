def filter_list(lst, a):
    if a == 0:
        for number in lst:
            print(number)
            if number % 2 == 0:
                lst.remove(number)
        return lst
    else:
        for number in lst:
            print(number)
            if number % 2 == 1:
                # print(number)
                lst.remove(number)
        return lst
    
print(filter_list([3, 5, 3, 6], 1))
print(filter_list([3, 5, 3, 6], 1))


