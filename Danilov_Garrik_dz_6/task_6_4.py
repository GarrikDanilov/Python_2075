# Задание 4

import sys


def gen_dataset(path_users_file: str, path_hobby_file: str):
    with open(path_users_file, 'r', encoding='utf-8') as users_fr:
        with open(path_hobby_file, 'r', encoding='utf-8') as hobby_fr:
            while True:
                user = users_fr.readline().strip()
                hobby = hobby_fr.readline().strip()
                if not user and not hobby:
                    break
                if hobby:
                    yield f'{user}: {hobby}\n'
                else:
                    yield f'{user}: {None}\n'


# Предварительная проверка исходных файлов
with open('users.csv', 'r', encoding='utf-8') as u_fr:
    with open('hobby.csv', 'r', encoding='utf-8') as h_fr:
        while True:
            users = u_fr.readline().strip()
            hobbies = h_fr.readline().strip()
            if not users and hobbies:
                sys.exit(1)
            if not users and not hobbies:
                break
with open('users_hobby.txt', 'w', encoding='utf-8') as fw:
    fw.writelines(gen_dataset('users.csv', 'hobby.csv'))
