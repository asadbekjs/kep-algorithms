# 123 => "123" => "1", "2", "3"
def sum_digits(number):
    s = 0
    for digit in str(number):
        raqam = int(digit)
        s += raqam

    return s

# print(sum_digits(123)) # 6
n = input() # "123456"
start = n[0:3]
end = n[3:6]
print(sum_digits(start) == sum_digits(end))