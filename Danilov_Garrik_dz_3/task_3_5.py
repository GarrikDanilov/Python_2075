# Задание 5

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    for _ in range(count):
        list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return list_out


# Вывод результата выполнения функции get_jokes
print(get_jokes(2))
print(get_jokes(10))


def get_jokes_adv(count=1, flag=0):
    if not flag:
        return get_jokes(count)
    min_count = min((len(nouns), len(adverbs), len(adjectives)))
    if min_count < count:
        return f'Количество шуток должно быть не более {min_count}'
    list_jokes = get_jokes(1)

    def check_match(word: str):
        for string in list_jokes:
            if string.find(word) > -1:
                return False
        return True

    for _ in range(1, count):
        list_jokes.append(
            f'{choice(list(filter(check_match, nouns)))} '
            f'{choice(list(filter(check_match, adverbs)))} '
            f'{choice(list(filter(check_match, adjectives)))}')
    return list_jokes


# Вывод результата выполнения функции get_jokes_adv
print(get_jokes_adv(5, 1))
