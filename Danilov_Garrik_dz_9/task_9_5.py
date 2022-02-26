# Задание 5


class Stationary:
    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> None:
        print('Запуск отрисовки')


class Pen(Stationary):
    def draw(self) -> None:
        print(f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"')


class Pencil(Stationary):
    def draw(self) -> None:
        super().draw()
        print(f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"')


class Handle(Stationary):
    def draw(self) -> None:
        print(f'{self.__class__.__name__}: приступил к отрисовке объекта "{self.title}"')


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()
    handle.draw()
    pencil.draw()
