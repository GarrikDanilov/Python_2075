# Задание 3

# Функция, выполняющая склонение слова "процент"
def transform_string(number: int):
    if 11 <= number % 100 <= 14:
        return f'{number} процентов'
    elif number % 10 == 1:
        return f'{number} процент'
    elif 2 <= number % 10 <= 4:
        return f'{number} процента'
    else:
        return f'{number} процентов'


# Проверка работы программы для чисел от 1 до 100
for n in range(1, 101):
    print(transform_string(n))
