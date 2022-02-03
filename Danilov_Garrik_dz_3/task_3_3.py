# Задание 3


def thesaurus(*args) -> dict:
    dict_out = {}
    for name in args:
        if name[0] in dict_out:
            dict_out[name[0]].append(name)
        else:
            dict_out[name[0]] = [name]
    return dict_out


# Вывод результата
print(thesaurus("Иван", "Мария", "Петр", "Илья"))

# Вывод результата с сортировкой по ключам
print('\n')
print('Вывод результата с сортировкой по ключам')
my_dict = thesaurus("Иван", "Мария", "Петр", "Илья")
for key in sorted(my_dict):
    print(f"'{key}':", my_dict[key])
