# Задание 2

# Создание списка кубов нечетных чисел от 1 до 1000
my_list = []
for odd_number in range(1, 1000, 2):
    my_list.append(odd_number**3)


# a) Функция вычисления суммы чисел из my_list, сумма цифр которых делится нацело на 7
def sum_list_1(dataset: list):
    sum_list = 0
    for index, number in enumerate(dataset):
        number_sum = 0
        while True:
            number_sum += number % 10
            if not number // 10:
                if not number_sum % 7:
                    sum_list += dataset[index]
                break
            number = number // 10
    return sum_list


# b) Функция вычисления суммы чисел из списка, составленного из списка my_list, к каждому элементу которого добавлено
# число 17
def sum_list_2(dataset: list):
    new_list = []
    for number in dataset:
        new_list.append(number + 17)
    sum_list = 0
    for index, number in enumerate(new_list):
        number_sum = 0
        while True:
            number_sum += number % 10
            if not number // 10:
                if not number_sum % 7:
                    sum_list += new_list[index]
                break
            number = number // 10
    return sum_list


# c) Функция вычисления суммы чисел из списка, составленного из списка my_list, к каждому элементу которого добавлено
# число 17. Без создания нового списка
def sum_list_3(dataset: list):
    sum_list = 0
    for index, number in enumerate(dataset):
        number += 17
        number_sum = 0
        while True:
            number_sum += number % 10
            if not number // 10:
                if not number_sum % 7:
                    sum_list += dataset[index] + 17
                break
            number = number // 10
    return sum_list


# Вывод результатов работы программы
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
result_3 = sum_list_3(my_list)
print(result_3)
