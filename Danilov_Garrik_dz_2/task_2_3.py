# Задание 3

my_list = ['в', '5', 'часов', '17', 'минут', 'температура',
           'воздуха', 'была', '+5', 'градусов']


# Вариант 1
def convert_list_in_str(list_in: list):
    str_out = f' {" ".join(list_in)} '
    for string in list_in:
        if string[0].isdigit():
            str_out = str_out.replace(f' {string} ',
                                      f' \"{int(string):02d}\" ')
        elif len(string) >= 2 and string[1].isdigit():
            str_out = str_out.replace(f' {string} ',
                                      f' \"{string[0]}{int(string[1:]):02d}\" ')
    str_out = str_out.lstrip().rstrip()
    return str_out


result = convert_list_in_str(my_list)
print(result)


# Вариант 2
def convert_list_in_str2(list_in: list):
    for index in range(len(list_in)):
        if list_in[index][0].isdigit():
            list_in[index] = (f'\"{int(list_in[index]):02d}\"')
        elif len(list_in[index]) >= 2 and list_in[index][1].isdigit():
            list_in[index] = (f'\"{list_in[index][0]}'
                              f'{int(list_in[index][1:]):02d}\"')
    str_out = ' '.join(list_in)
    return str_out

result2 = convert_list_in_str2(my_list)
print(result2)
