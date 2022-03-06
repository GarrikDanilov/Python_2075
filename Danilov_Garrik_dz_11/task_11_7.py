# Задание 7


class ComplexObject:
    def __init__(self, real: int | float = 0, image: int | float = 0):
        if not isinstance(real, int) or isinstance(real, float):
            raise TypeError('Тип аргумента real должен быть: int, float')
        if not isinstance(image, int) or isinstance(image, float):
            raise TypeError('Тип аргумента image должен быть: int, float')
        self.real = real
        self.image = image

    def __add__(self, other):
        if isinstance(other, ComplexObject):
            return ComplexObject(self.real + other.real, self.image + other.image)
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexObject(self.real + other, self.image)
        else:
            raise TypeError('Операция возможна над типами: ComplexObject, int, float')

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, ComplexObject):
            real = self.real * other.real - self.image * other.image
            image = self.real * other.image + other.real * self.image
            return ComplexObject(real, image)
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexObject(self.real * other, self.image * other)
        else:
            raise TypeError('Операция возможна над типами: ComplexObject, int, float')

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        if not self.real and not self.image:
            return str(0)
        elif not self.real:
            return f'{self.image}j'
        elif not self.image:
            return str(self.real)
        else:
            return f'{self.real}{"+" if self.image > 0 else ""}{self.image}j'


if __name__ == '__main__':
    a = ComplexObject(5, 7)
    b = ComplexObject(3, -4)
    c = a + b
    print(c)
    c = a * b
    print(c)
    d = ComplexObject(3, '-4')
