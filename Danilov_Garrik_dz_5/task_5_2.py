# Задание 2


def odd_nums_adv(number: int):
    return (odd_number for odd_number in range(1, number +1, 2))


n = 15
generator = odd_nums_adv(n)
for _ in range(1, n + 1, 2):
    print(next(generator))
# next(generator)
