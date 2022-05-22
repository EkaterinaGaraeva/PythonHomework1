# Пользователь задаёт две строки. 
# Определить количество вхождений одной строки в другой.

def count(str1, str2):
    count = 0
    for i in range(0, len(str1)):
        for j in range(0, len(str2)):
            if str2[j] == str1[i]:
                count += 1
    print(count)

print(f'Введите первую строку')
srtring_one = input()
print(f'Введите вторую строку')
string_two = input()
count(srtring_one, string_two)
