# Задание 4


def thesaurus_adv(*args):
    dict_out = {}
    for first_name, last_name in map(lambda name: name.split(' '), args):
        dict_out.setdefault(last_name[0], {}).setdefault(first_name[0], []).append(f'{first_name} {last_name}')
    return dict_out


# Вывод результата
print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))

# Вывод результата с сортировкой по ключам
print('\n')
print('Вывод результата с сортировкой по ключам')
my_dict = thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')


def dict_sorted(dict_in: dict):
    for first_key in sorted(dict_in):
        print(f"'{first_key}':", dict_in[first_key])


for key in sorted(my_dict):
    print(f"'{key}':", "{")
    dict_sorted(my_dict[key])
    print("}")
