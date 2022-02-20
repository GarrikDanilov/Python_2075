# Задание 3
# Выполнено в виде CLI

import os
import shutil
import sys
from shutil import copy2


def main(argv):
    """
    Принимает в качестве аргумента путь к папке со структурой проекта
    и создает в указанной папке папку templates, содержащую все шаблоны проекта

    :param argv: путь к папке со структурой проекта
    :return: создает папку templates, содержащую все шаблоны проекта
    """
    if not os.path.exists(argv[1]):
        print('Директория не найдена')
        return 1
    for root, dirs, files in os.walk(argv[1]):
        if files:
            for f_name in files:
                if f_name.endswith('.html'):
                    src_path = os.path.join(root, f_name)
                    dst_path = os.path.join(argv[1], 'templates', os.path.basename(root), f_name)
                    try:
                        if os.path.exists(dst_path):
                            raise FileExistsError
                        copy2(src_path, dst_path)
                    except FileNotFoundError:
                        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                        copy2(src_path, dst_path)
                    except (shutil.SameFileError, FileExistsError):
                        if src_path == dst_path:
                            pass
                        else:
                            if input(f'Файл {src_path} уже существует в templates. Копировать с заменой Y/N: ') == 'Y':
                                os.remove(dst_path)
                                copy2(src_path, dst_path)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
