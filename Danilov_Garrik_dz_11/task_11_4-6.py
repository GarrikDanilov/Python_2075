# Задания 4-6

from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    __owner = None

    def __init__(self, name: str, serial_number: str):
        self._model = name
        self._serial_number = serial_number

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner):
        self.__owner = owner

    @abstractmethod
    def title(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

    def __str__(self):
        return f'{self.__class__.__name__} model: {self._model}. S/N: {self._serial_number}'


class Printer(OfficeEquipment):
    __title = 'Принтер'
    _is_color: bool = False
    _printer_type: str = 'Laser'
    _paper_formats: tuple = 'A4'

    def __init__(self, name: str, serial_number: str, **kwargs):
        super().__init__(name, serial_number)
        if 'color' in kwargs and isinstance(kwargs['color'], bool):
            self._is_color = kwargs['color']
        if 'type' in kwargs and kwargs['type'] in ('Laser', 'Inkjet'):
            self._printer_type = kwargs['type']
        if 'formats' in kwargs and self.__check_formats(kwargs['formats']):
            self._paper_formats = kwargs['formats']

    @staticmethod
    def __check_formats(formats):
        list_formats = 'A4', 'A3', 'A2', 'A1', 'A0'
        if isinstance(formats, str):
            return formats in list_formats
        elif isinstance(formats, tuple):
            return all([item in list_formats for item in formats])
        else:
            return False

    @property
    def title(self):
        return self.__title

    def get_info(self):
        return f'{"Лазерный" if self._printer_type == "Laser" else "Струйный"} ' \
               f'{"черно-белый" if self._is_color == False else "цветной"} принтер {self._model}.', \
               f'Серийный номер: {self._serial_number}.', \
               f'Печать возможна на листах формата: ' \
               f'{", ".join(self._paper_formats) if isinstance(self._paper_formats, tuple) else self._paper_formats}'


class Scanner(OfficeEquipment):
    __title = 'Сканер'
    _scanner_type: str = 'Flatbed'

    def __init__(self, name: str, serial_number: str, scanner_type: str = None):
        super().__init__(name, serial_number)
        if scanner_type and scanner_type in ('Flatbed', 'Broach'):
            self._scanner_type = scanner_type

    @property
    def title(self):
        return self.__title

    def get_info(self):
        return f'{"Планшетный" if self._scanner_type == "Flatbed" else "Протяжной"} сканер {self._model}.', \
               f'Серийный номер: {self._serial_number}.'


class Xerox(Printer):
    __title = 'Ксерокс'

    @property
    def title(self):
        return self.__title

    def get_info(self):
        return f'{"Лазерный" if self._printer_type == "Laser" else "Струйный"} ' \
               f'{"черно-белый" if self._is_color == False else "цветной"} ксерокс {self._model}.', \
               f'Серийный номер: {self._serial_number}.', \
               f'Печать возможна на листах формата: ' \
               f'{", ".join(self._paper_formats) if isinstance(self._paper_formats, tuple) else self._paper_formats}'


class Warehouse:
    def __init__(self, name: str):
        self.__name = name
        self.__list_equipment = dict()

    def put_equipment(self, *equipment: OfficeEquipment):
        if not self.__check_equipment(*equipment):
            raise TypeError('Объект(ы) не оргтехника')

        for item in equipment:
            self.__list_equipment.setdefault(item.title, []).append(item)
            item.owner = self

    def get_equipment(self, equipment: str, count: int):
        if not isinstance(equipment, str):
            raise TypeError('Тип оргтехники должен быть строкой')
        if equipment not in self.__list_equipment:
            raise ValueError(f'На складе нет оргтехники типа {equipment}')
        if not isinstance(count, int):
            raise TypeError('Количество оргтехники должно быть целым числом')
        available = len(self.__list_equipment[equipment])
        if available < count:
            raise ValueError(f'В наличии только {available} шт.')

        list_out = []
        for _ in range(count):
            temp = self.__list_equipment[equipment].pop()
            temp.owner = None
            list_out.append(temp)
        if not self.__list_equipment[equipment]:
            self.__list_equipment.pop(equipment)
        return list_out

    @staticmethod
    def __check_equipment(*equipment):
        for item in equipment:
            if not isinstance(item, OfficeEquipment):
                return False
        return True

    def get_info(self):
        if not len(self.__list_equipment):
            print(f'{self.__name} оргтехники не имеет')
            return
        print(f'{self.__name} имеет на хранении следующую оргтехнику:')
        for key, value in self.__list_equipment.items():
            print(f'\t- оргтехника типа "{key}":')
            for item in value:
                print('\t\t-', *item.get_info())


if __name__ == '__main__':
    printer_1 = Printer('Canon', '123AB45', color=True, type='Inkjet')
    printer_2 = Printer('Pantum', '124SB89')
    printer_3 = Printer('HP', '124SB90', color=True, formats=('A4', 'A3'))
    xerox_1 = Xerox('Ricoh', '123AZ67')
    scaner_1 = Scanner('Epson', '123AZ67')
    scaner_2 = Scanner('Plustek', '123AZ68', scanner_type='Broach')
    office_warehouse = Warehouse('Склад оргтехники')
    office_warehouse.put_equipment(printer_1, printer_2, printer_3, xerox_1, scaner_1, scaner_2)
    office_warehouse.get_info()
    print('\n\n')
    department = Warehouse('Подразделение 0001')
    department.put_equipment(*office_warehouse.get_equipment('Принтер', 2))
    department.put_equipment(*office_warehouse.get_equipment('Ксерокс', 1))
    office_warehouse.get_info()
    print('\n\n')
    department.get_info()
    department.put_equipment(*office_warehouse.get_equipment('Ксерокс', 1))
