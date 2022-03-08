# Задание 3

import re


class CheckValue(Exception):
    def __init__(self, value):
        self.value = value
        self.result = CheckValue.__check_value(value)

    @staticmethod
    def __check_value(value):
        return re.match(r'^[+-]?\d+([,.]?\d+)*\d*$', value)

    def __str__(self):
        if self.result:
            return f'Введено число {self.value}'
        else:
            return f'Введенное значение "{self.value}" не является числом'


if __name__ == '__main__':
    list_out = []
    while True:
        resp = input('Введите чило (для выхода введите stop): ')
        try:
            if resp != 'stop':
                raise CheckValue(resp)
        except CheckValue as check:
            if check.result:
                list_out.append(resp)
            else:
                print(check)
        else:
            print(list_out)
            break
