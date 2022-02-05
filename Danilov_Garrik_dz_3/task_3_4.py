# Задание 4


def thesaurus_adv(*args):
    dict_out = {}
    for first_name, last_name in map(lambda string: string.split(' '), args):
        if last_name[0] in dict_out:
            if first_name[0] in dict_out[last_name[0]]:
                dict_out[last_name[0]][first_name[0]].append(f'{first_name} {last_name}')
            else:
                dict_out[last_name[0]].update({first_name[0]: [f'{first_name} {last_name}']})
        else:
            dict_out[last_name[0]] = {first_name[0]: [f'{first_name} {last_name}']}
    return dict_out


# Вывод результата
print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))

# Вывод результата с сортировкой по ключам
print('\n')
print('Вывод результата с сортировкой по ключам')
my_dict = thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева')


def dict_sorted(dict_in: dict):
    for key in sorted(dict_in):
        print(f"'{key}':", dict_in[key])


for key in sorted(my_dict):
    print(f"'{key}':", "{")
    dict_sorted(my_dict[key])
    print("}")
