import sys
from add_sale import MAX_LEN


def main(argv):
    if len(argv) == 1:
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            for line in fr:
                print(line.strip())
    elif len(argv) == 2:
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            fr.seek(((MAX_LEN + 2) * (int(argv[1]) - 1)), 0)
            for line in fr:
                print(line.strip())
    elif len(argv) == 3:
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            fr.seek(((MAX_LEN + 2) * (int(argv[1]) - 1)), 0)
            for index, line in enumerate(fr):
                print(line.strip())
                if index == int(argv[2]) - int(argv[1]):
                    break
    else:
        print('Превышено количество аргументов. Должно быть не более 2')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
