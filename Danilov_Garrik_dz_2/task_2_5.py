# Задание 5

# Создание списка цен на товары
from random import uniform
my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]

# a) Вывод строки, содержащей цены в формате <r> руб <kk> коп


# Функция преобразования в строку
def transfer_list_in_str(list_in: list):
    list_prices = []
    for cost in list_in:
        list_prices.append(f'{int(cost)} руб {int(round(cost % 1, 2) * 100):02d} коп')
    str_out = ', '.join(list_prices)
    return str_out


# Вывод строки
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)

# b) Сортировка списка цен по возрастанию


# Функция сортировки
def sort_prices(list_in: list):
    list_in.sort()
    return list_in


# Вывод результата
print(f'Адрес исходного списка: {id(my_list)}')
result_2 = sort_prices(my_list)
print(f'Адрес списка, упорядоченного по возрастанию: {id(result_2)}')
print(result_2)

# b) Сортировка списка цен по убыванию


# Функция сортировки
def sort_price_adv(list_in: list):
    list_out = sorted(list_in, reverse=True)
    return list_out


# Вывод результата
result_3 = sort_price_adv(my_list)
print(result_3)

# Вывод цены пяти самых дорогих товаров


# Функция сортировки и вывода цен
def check_five_max_elements(list_in: list):
    list_out = sorted(list_in)[-5:]
    return list_out


# Вывод результата
result_4 = check_five_max_elements(my_list)
print(result_4)
