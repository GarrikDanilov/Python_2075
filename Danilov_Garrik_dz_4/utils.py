import requests


def currency_rates(code: str):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    valute_info = response.text
    valute_index = valute_info.find(code.upper())
    if valute_index != -1:
        valute_info = valute_info[valute_index:valute_info.find('</Value>', valute_index)]
        nominal = float(valute_info[valute_info.find('<Nominal>') + 9:
                                    valute_info.find('</Nominal>')].replace(',', '.'))
        value = float(valute_info[valute_info.find('<Value>') + 7:].replace(',', '.'))
        response.close()
    else:
        response.close()
        return
    result_value = round(value / nominal, 4)
    return result_value

if __name__ == '__main__':
    print(currency_rates("USD"))
    print(currency_rates("eur"))
    print(currency_rates("noname"))