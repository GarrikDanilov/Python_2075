# Задание 3

import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    pass


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, ensure_ascii=False, indent=2)