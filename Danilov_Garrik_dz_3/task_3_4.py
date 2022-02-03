# Задание 4


def thesaurus_adv(*args):
    dict_out = {}
    first_name = []
    last_name = []
    for name in args:
        n1, n2 = name.split(' ')
        first_name.append(n1)
        last_name.append(n2)
    for fname, lname in zip(first_name, last_name):
        if lname[0] in dict_out:
            pass
        else:
            dict_out[lname[0]] = {fname[0]: [f'{fname} {lname}']}
    pass
    print(first_name, '\n', last_name)
    return dict_out


# Вывод результата
print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))
