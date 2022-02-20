# Задание 5
# Выполнено в виде CLI

import os
import json
import sys


def check_file_size(cur_file):
    step = 10
    file_extension = f'.{cur_file.name.rsplit(".", 1)[1]}'
    if not cur_file.stat().st_size:
        return 0, file_extension
    while cur_file.stat().st_size // step:
        if cur_file.stat().st_size == step:
            break
        step *= 10
    return step, file_extension


def main(argv):
    """
    Принимает в качестве аргумента путь к папке и выводит статистику для заданной папки в виде словаря,
    в котором ключи — верхняя граница размера файла (кратна 10), а значения — список из общего количества файлов
    (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начиная с 0) и их
    расширений.
    Сохраняет результат в фай <имя папки>_summary.json, расположенный в корне анализируемой папки

    :param argv: путь до заданной папки
    :return: Словарь - порог размера файла (с шагом 10): [количество файлов, расширения]
    """
    if not os.path.exists(argv[1]):
        print('Директория не найдена')
        return 1
    dict_out = dict()
    for root, dirs, files in os.walk(argv[1]):
        if files:
            for item in os.scandir(root):
                if item.is_file(follow_symlinks=False):
                    item_key, extension = check_file_size(item)
                    if item_key not in dict_out:
                        dict_out[item_key] = (1, [extension])
                    elif extension in dict_out[item_key][1]:
                        dict_out[item_key] = (dict_out[item_key][0] + 1, dict_out[item_key][1])
                    else:
                        dict_out[item_key][1].append(extension)
                        dict_out[item_key] = (dict_out[item_key][0] + 1, dict_out[item_key][1])
    print(dict_out)
    with open(os.path.join(argv[1], f'{os.path.basename(argv[1])}_summary.json'), 'w', encoding='utf-8') as fw:
        json.dump(dict_out, fw, indent=2)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
