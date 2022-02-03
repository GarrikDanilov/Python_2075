# Задание 1

numerals = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
            'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
            'eight': 'восемь', 'nine': 'девять'
            }


def num_translate(value: str) -> str:
    """Переводит числительные с английского на русский"""
    str_out = numerals.get(value)
    return str_out


# Вывод результата
print(num_translate('one'))
print(num_translate('eight'))
