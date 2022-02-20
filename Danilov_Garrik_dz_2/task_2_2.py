# Задание 2


def convert_list_in_str(list_in: list):
    new_list = []
    for string in list_in:
        if string[0].isdigit():
            new_list.append(f'\"{int(string):02d}\"')
        elif len(string) >= 2 and string[1].isdigit():
            new_list.append(f'\"{string[0]}{int(string[1:]):02d}\"')
        else:
            new_list.append(string)
    str_out = ' '.join(new_list)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']

result = convert_list_in_str(my_list)
print(result)
