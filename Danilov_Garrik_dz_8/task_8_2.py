# Задание 2

import re


def parse_line(line: str) -> tuple:
    RE_LOG = re.compile(r'(?P<remote_addr>(?:^\d{1,3}(?:\.\d{1,3}){3})|(?:^[0-f0-F]{1,4}(?::[0-f0-F]{1,4}){7})|'
                        r'(?:^[0-f0-F]{1,4}(?::[0-f0-F]{0,4}){3,7})|(?:^[0-f0-F]{0,4}(?::[0-f0-F]{0,4}){2})).*'
                        r'(?P<request_datetime>\[.*]).*(?P<request_type>GET|POST|HEAD).*?'
                        r'(?P<requested_resource>/.+?)".*?(?P<response_code>\d{3}).*?(?P<response_size>\d+)')
    tuple_out = RE_LOG.match(line).group('remote_addr', 'request_datetime', 'request_type',
                                         'requested_resource', 'response_code', 'response_size')
    return tuple_out


with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        print(parse_line(line))
