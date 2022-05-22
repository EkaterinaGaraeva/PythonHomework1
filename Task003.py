# Подсчитать сумму цифр в вещественном числе.

def sum_numbers(number):
    sum = 0
    string_number = str(number)
    for i in range(0, len(string_number)):
        if string_number[i] != ".":
            sum += int(string_number[i])
    print(sum)

sum_numbers(123.456)
