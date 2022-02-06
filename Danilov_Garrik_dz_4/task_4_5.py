# Задание 4

import sys
import utils


def main(argv):
    program, args = argv
    print(utils.currency_rates(args))
    return 0


exit(main(sys.argv))

"""
PS D:\My_Python\Python_2075\Danilov_Garrik_dz_4> python task_4_5.py BYN
29.5194
PS D:\My_Python\Python_2075\Danilov_Garrik_dz_4> python task_4_5.py noname
None
"""
