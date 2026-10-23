## базовый класс для всех фигур
class Shape:
    def area(self):
        # пустой метод, который перепишем у наследников
        return 0.0

    def perimeter(self):
        # пустой метод для переписывания в наследниках
        return 0.0


## первый наследник: круг
class круг(Shape):
    def __init__(self, radius):
        self.radius = radius

    ## переопределение методов
    def area(self):
        pi = 3.14159
        return pi * (self.radius ** 2)

    def perimeter(self):
        pi = 3.14159
        return 2 * pi * self.radius


## второй наследник: прямоугольник
class прямоугольник(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    ## переопределение методов
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


## третий наследник: треугольник
class треугольник(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    ## переопределение методов
    def area(self):
        # считаем площадь по трем сторонам
        p = (self.a + self.b + self.c) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

## ввод данных с клавиатуры
# запрашиваем данные для круга
r = float(input("введите радиус круга: "))

# запрашиваем данные для прямоугольника
w = float(input("введите ширину прямоугольника: "))
h = float(input("введите высоту прямоугольника: "))

# запрашиваем данные для треугольника
t_a = float(input("введите 1 сторону треугольника: "))
t_b = float(input("введите 2 сторону треугольника: "))
t_c = float(input("введите 3 сторону треугольника: "))

## проверка работы программы
# делаем список из разных фигур
figures = [
    круг(r),
    прямоугольник(w, h),
    треугольник(t_a, t_b, t_c)
]

print("результаты расчета фигур:")

# один цикл считает данные для всех фигур подряд
for fig in figures:
    # выводим название фигуры, площадь и периметр
    print(f"\nфигура: {fig.__class__.__name__}")
    print(f"площадь = {round(fig.area(), 2)}")
    print(f"периметр = {round(fig.perimeter(), 2)}")
