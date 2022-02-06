# Задание 3

import datetime
import requests


def currency_rates_adv(code: str):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    valute_info = response.text
    valute_index = valute_info.find(code.upper())
    if valute_index != -1:
        curs_day, curs_month, curs_year = valute_info[valute_info.find('Date') + 6:
                                                      valute_info.find('" name')].split('.')
        valute_info = valute_info[valute_index:valute_info.find('</Value>', valute_index)]
        nominal = float(valute_info[valute_info.find('<Nominal>') + 9:
                                    valute_info.find('</Nominal>')].replace(',', '.'))
        value = float(valute_info[valute_info.find('<Value>') + 7:].replace(',', '.'))
        response.close()
    else:
        response.close()
        return
    result_value = round(value / nominal, 4)
    data_value = datetime.date(int(curs_year), int(curs_month), int(curs_day))
    return result_value, data_value


kurs, date_value = currency_rates_adv("USD")

empty = bool(not kurs and not date_value)
if not empty and not isinstance(kurs, float):
    raise TypeError("Неверный тип данных у курса")
if not empty and not isinstance(date_value, datetime.date):
    raise TypeError("Неверный тип данных у даты")
print(kurs, date_value)
