# Задание 2

numerals = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три',
            'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
            'eight': 'восемь', 'nine': 'девять'
            }


def num_translate_adv(value: str) -> str:
    """Переводит числительные с английского на русский"""
    str_out = numerals.get(value.lower())
    if str_out is not None and value.istitle():
        str_out = str_out.title()
    return str_out


# Вывод результата
print(num_translate_adv('One'))
print(num_translate_adv('two'))
