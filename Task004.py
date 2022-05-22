# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def sequence(n):
    numbers = list(range(1, n + 1))
    for i in range(1, n):
        numbers[i] = numbers[i - 1] * (i + 1)
    print(numbers)

sequence(4)
