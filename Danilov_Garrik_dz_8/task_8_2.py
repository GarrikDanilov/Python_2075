# Задание 2

import re


def parse_line(line: str) -> tuple:
    RE_LOG = re.compile(r'(?P<remote_addr>^\d{1,3}(?:\.\d{1,3}){3}).*'
                        r'(?P<request_datetime>\[.*]).*"(?P<request_type>[A-Z]{3,4})')
    tuple_out = RE_LOG.match(line).group('remote_addr', 'request_datetime', 'request_type')
    return tuple_out


with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    print(parse_line(fr.readline()))

