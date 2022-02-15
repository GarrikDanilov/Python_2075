# Задание 1

from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    remote_addr = line[:line.find(' ')]
    request_type = line[line.find('"') + 1:line.find(' ', line.find('"'))]
    requested_resource = line[line.find(' /') + 1:line.find(' ', line.find(' /') + 1)]
    return remote_addr, request_type, requested_resource


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for one_line in fr:
        list_out.append(get_parse_attrs(one_line))

pprint(list_out)
