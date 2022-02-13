import sys

MAX_LEN = 12


def main(argv):
    if len(argv) != 2:
        print('Неверное количество аргументов\n',
              f'Введено: {len(argv) - 1}\n', 'Должно быть: 1')
        return 1
    with open('bakery.csv', 'a', encoding='utf-8') as fw:
        fw.write(f'{argv[1]:{MAX_LEN}}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
