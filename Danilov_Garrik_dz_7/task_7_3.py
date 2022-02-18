# Задание 3
# Выполнено в виде CLI

import os
import sys


def main(argv):
    for root, dirs, files in os.walk(argv[1]):
        print(dirs)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
