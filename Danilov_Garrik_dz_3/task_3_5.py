# Задание 5

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """
    Возвращает список шуток в количестве count

    :param count: количество шуток
    :type count: int
    :return: list_out[str] список шуток
    :rtype: list
    """
    list_out = []
    for _ in range(count):
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return list_out


# Вывод результата выполнения функции get_jokes
print(get_jokes(2))
print(get_jokes(10))


def get_jokes_adv(count: int, flag: int = 0) -> list:
    """
        Возвращает список шуток в количестве count

        :param count: количество шуток
        :type count: int
        :param flag: аргумент, разрешающий (flag=0) или
             запрещающий (flag=1) повторы слов в шутках, defaults to 0
        :type flag: int
        :rtype: list
        :return: list_out[str] список шуток
    """
    if not count:
        return []
    if not flag:
        return get_jokes(count)
    min_count = min((len(nouns), len(adverbs), len(adjectives)))
    if min_count < count:
        print(f'Количество шуток должно быть не более {min_count}')
        return []

    # Функция определения повторяющихся слов
    def check_match(word: str):
        for string in list_jokes:
            if string.find(word) == -1:
                pass
            elif string.find(word) == 0 or string[string.find(word) - 1].isspace():
                return False
        return True

    list_jokes = get_jokes(1)
    for _ in range(1, count):
        list_jokes.append(
            f'{choice(list(filter(check_match, nouns)))} '
            f'{choice(list(filter(check_match, adverbs)))} '
            f'{choice(list(filter(check_match, adjectives)))}')
    return list_jokes


# Вывод результата выполнения функции get_jokes_adv
print(get_jokes_adv(5, flag=1))
