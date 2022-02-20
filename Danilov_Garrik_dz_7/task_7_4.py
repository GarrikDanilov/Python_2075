# Задание 4
# Выполнено в виде CLI

import os
import sys


def check_file_size(cur_file):
    step = 10
    if not cur_file.st_size:
        return 0
    while cur_file.st_size // step:
        if cur_file.st_size == step:
            break
        step *= 10
    return step


def main(argv):
    """
    Принимает в качестве аргумента путь к папке и выводит статистику для заданной папки в виде словаря,
    в котором ключи — верхняя граница размера файла (кратна 10), а значения — общее количество файлов
    (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начиная с 0)

    :param argv: путь до заданной папки
    :return: Словарь - порог размера файла (с шагом 10): количество файлов
    """
    if not os.path.exists(argv[1]):
        print('Директория не найдена')
        return 1
    dict_out = dict()
    for root, dirs, files in os.walk(argv[1]):
        if files:
            for item in os.scandir(root):
                if item.is_file(follow_symlinks=False):
                    item_key = check_file_size(item.stat())
                    if item_key not in dict_out:
                        dict_out[item_key] = 1
                    else:
                        dict_out[item_key] += 1
    print(dict_out)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
