# Задание 3

import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
        Считывает данные из файлов и возвращает словарь, где:
            ключ — ФИО, значение — данные о хобби (список строковых переменных)
        :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
        :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
        :return: Dict(str: Union[List[str]|None])
    """
    with open(path_users_file, 'r', encoding='utf-8') as fr:
        list_users = [line.strip().replace(',', ' ') for line in fr if line.strip()]
    with open(path_hobby_file, 'r', encoding='utf-8') as fr:
        list_hobby = [line.strip().split(',') for line in fr if line.strip()]
    if len(list_users) < len(list_hobby):
        sys.exit(1)
    return {user: (list_hobby[index] if index < len(list_hobby) else None)
            for index, user in enumerate(list_users)}


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)

"""
1)
{
  "Иванов Иван Иванович": [
    "скалолазание",
    "охота"
  ],
  "Петров Петр Петрович": [
    "горные лыжи"
  ]
}

2)
{
  "Иванов Иван Иванович": [
    "скалолазание",
    "охота"
  ],
  "Петров Петр Петрович": null
}
В словаре по ключу "Петров Петр Петрович" значение None, но при сериализации в файле .json 
None заменяется на null
"""
