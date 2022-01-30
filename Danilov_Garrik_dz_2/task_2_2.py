# Задание 2


def convert_list_in_str(list_in: list):
    new_list = []
    for index in range(0, len(list_in)):
        if list_in[index][0].isdigit():
            new_list.extend(['"', f'{int(list_in[index]):02d}', '"'])
        elif len(list_in[index]) >= 2 and list_in[index][1].isdigit():
            new_list.extend(['"', f'{list_in[index][0]}{int(list_in[index][1:]):02d}', '"'])
        else:
            new_list.append(list_in[index])
    str_out = ''.join(new_list)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']

result = convert_list_in_str(my_list)
print(result)
