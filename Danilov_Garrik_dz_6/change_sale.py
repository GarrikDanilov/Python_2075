import sys
from add_sale import MAX_LEN


def main(argv):
    if len(argv) == 3:
        with open('bakery.csv', 'r+', encoding='utf-8') as fr:
            index = fr.seek(((MAX_LEN + 2) * (int(argv[1]) - 1)), 0)
            if not fr.readline():
                print('Введеный номер записи не существует')
                return 1
            fr.seek(index, 0)
            fr.write(f'{argv[2]:{MAX_LEN}}\n')
    else:
        print('Неверное количество аргументов\n',
              f'Введено: {len(argv) - 1}\n', 'Должно быть: 2')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))