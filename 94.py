# Algorithm:
# 1. Barcha 3 xonali sonlar
# 2. Raqamlar ko'paytmasini topuvchi function
# 3. Raqamlar yig'indisini topuvchi function
def calculate(number):
    # n = 729 => "729" => "7", "2", "9"
    p, s = 1, 0 
    for digit in str(number):
        p *= int(digit)
        s += int(digit)

    return p, s

for number in range(100, 1000):
    p, s = calculate(number)
    if p % s == 0:
        print(number)