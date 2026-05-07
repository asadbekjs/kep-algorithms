def divisors_count(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    return count

def map_divisors_count(sequence):
    return map(divisors_count, sequence)

print(list(map_divisors_count([-5, 12, 8])))

