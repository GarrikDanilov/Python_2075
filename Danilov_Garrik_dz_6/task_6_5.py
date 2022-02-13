# Задание 5

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


def main(argv):
    with open(argv[1], 'r', encoding='utf-8') as u_fr:
        with open(argv[2], 'r', encoding='utf-8') as h_fr:
            while True:
                users = u_fr.readline().strip()
                hobbies = h_fr.readline().strip()
                if not users and hobbies:
                    return 1
                if not users and not hobbies:
                    break
    with open(argv[3], 'w', encoding='utf-8') as fw:
        fw.writelines(gen_dataset(argv[1], argv[2]))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))

"""
PS D:\My_Python\Python_2075\Danilov_Garrik_dz_6> python task_6_5.py users.csv hobby.csv users_hobby2.txt

Файл users.csv:
Иванов,Иван,Иванович
Петров,Петр,Петрович

Файл hobby.csv:
скалолазание,охота

Файл users_hobby2.txt:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: None
"""