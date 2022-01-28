# Задание 1

# Функция преобразования времени
"""
1 мин = 60 сек
1 час = 3600 сек
1 дн = 86400 сек
"""
def convert_time(duration: int):
    if duration < 60:
        return f'{duration} сек'
    elif duration < 3600:
        return f'{duration // 60} мин {duration % 60} сек'
    elif duration < 86400:
        return f'{duration // 3600} час {duration % 3600 // 60} мин {duration % 60} сек'
    else:
        return f'{duration // 86400} дн {duration % 86400 // 3600} час {duration % 86400 % 3600 // 60} мин {duration % 60} сек'

# Проверка работы программы
duration = 400153
result = convert_time(duration)
print(result)

# Проверка работы программы в цикле
some_durations = [53, 153, 4153, 400153]
for duration in some_durations:
    result = convert_time(duration)
    print(result)
