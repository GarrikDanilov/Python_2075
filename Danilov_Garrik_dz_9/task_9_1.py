# Задание 1

from time import sleep


class TrafficLight:
    __color = 'red', 'yellow', 'green'

    def running(self):
        delays = 4, 2, 3
        for color, delay in zip(self.__color, delays):
            print(f'{color} {delay} сек')
            sleep(delay)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
