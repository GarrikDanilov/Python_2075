# Задание 1

import datetime


class MyDate:
    def __init__(self, date: str):
        date_in = MyDate.__check_date(date)
        if date_in:
            self.date = date_in
        else:
            raise ValueError('Введена некорректная дата')

    @staticmethod
    def __check_date(date: str):
        try:
            date_list = date.split('-')
            date_out = datetime.datetime.fromisoformat('-'.join(date_list[::-1]))
            return date_out
        except Exception:
            return None

    @classmethod
    def date_pars(cls, date: str):
        date_in = cls(date)
        return date_in.date.day, date_in.date.month, date_in.date.year


if __name__ == '__main__':
    result = MyDate.date_pars('30-12-2021')
    print(result)
    new_date = MyDate('32-12-2021')
