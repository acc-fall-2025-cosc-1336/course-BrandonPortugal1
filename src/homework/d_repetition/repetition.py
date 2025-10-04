def get_factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

def sum_odd_numbers(number):
    total = 0
    i = 1
    while i <= number:
        if i % 2 != 0:
            total += i
        i += 1
    return total