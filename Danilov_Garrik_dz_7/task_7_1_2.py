# Задание 1
# Выполнено в виде CLI

import os
import json
import shutil
import sys


def make_dir(dir_path, dir_content):
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    if isinstance(dir_content, list):
        for f_name in dir_content:
            f_path = os.path.join(dir_path, f_name)
            if not os.path.exists(f_path):
                open(f_path, 'w').close()
    elif isinstance(dir_content, dict):
        for names_dirs, content in dir_content.items():
            new_dir = os.path.join(dir_path, names_dirs)
            make_dir(new_dir, content)


def main(argv):
    """
    Принимает в качестве аргумента путь к файлу со структурой проекта
    и создает в дириктории с указанным файлом заготовку проекта в соответствии
    со структурой, указанной в файле
    :param argv: путь к файлу со структурой проекта
    :return: директория со структурой проекта
    """
    try:
        with open(argv[1], 'r', encoding='utf-8') as fr:
            prj_config = json.load(fr)
            prj_root, _ = os.path.split(argv[1])
            name_main_dir = list(prj_config.keys())[0]
            main_dir = os.path.join(prj_root, name_main_dir)
            os.mkdir(main_dir)
    except FileNotFoundError as no_file:
        print(f'Файл не найден: {no_file.filename}')
        return 1
    except FileExistsError as exist_dir:
        print(f'Директория: {exist_dir.filename} уже существует\n')
        if input('Создать заново (текущая директория и вложенные файлы и папки будут удалены) Y/N: ') == 'Y':
            shutil.rmtree(main_dir)
            os.mkdir(main_dir)
        else:
            return 1
    except OSError as other_err:
        print(f'Ошибка: {other_err}')
        return 1
    for names_dirs, content in prj_config[name_main_dir].items():
        new_dir = os.path.join(main_dir, names_dirs)
        make_dir(new_dir, content)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
