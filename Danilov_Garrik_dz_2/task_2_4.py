# Задание 4


# Функция обработки списка строк
def convert_name_extract(list_in: list):
    list_out = []
    for string in list_in:
        list_out.append(f'Привет, {string.split(" ")[-1].capitalize()}!')
    return list_out


# Вывод результата
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
           'токарь высшего разряда нИКОЛАЙ', 'директор аэлита'
           ]
result = convert_name_extract(my_list)
print(result)
