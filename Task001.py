# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def sequence(n):
    numbers = list(range(1, n + 1))
    for i in range(1, n):
        numbers[i] = numbers[i - 1] * -3
    print(numbers)

sequence(5)
