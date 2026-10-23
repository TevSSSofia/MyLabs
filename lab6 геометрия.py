## БЛОК ФУНКЦИЙ 
def calculate_circle_area(radius):
    "вычисляет площадь круга"
    pi = 3.14159
    return pi * (radius ** 2)

def calculate_triangle_area(a, b, c):
    "вычисляет площадь треугольника по формуле Герона"
# Полупериметр
    p = (a + b + c) / 2
# Формула Герона
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area

def calculate_rectangle_area(width, height):
    "Вычисляет площадь прямоугольника"
    return width * height


## БЛЛОК ВВОДА ДАННЫХ 


def input_circle():
    "запрашивает данные для круга и возвращает радиус"
    r = float(input("Введите радиус круга: "))
    if r <= 0:
        print("Ошибка: радиус должен быть больше нуля!")
        return None
    return r

def input_triangle():
    "запрашивает стороны треугольника с проверкой на существование"
    print("Введите три стороны треугольника через пробел:")
    sides = input().split()
    if len(sides) != 3:
        print("ошибка: нужно ввести ровно 3 числа")
        return None
        
    a = float(sides[0])
    b = float(sides[1])
    c = float(sides[2])
    
# Проверка неравенства триугольника 
    if a + b <= c or a + c <= b or b + c <= a:
        print("Ошибка: треугольник с такими сторонами не существует!")
        return None
    return a, b, c

def input_rectangle():
    """Запрашивает стороны прямоугольника."""
    w = float(input("Введите ширину прямоугольника: "))
    h = float(input("Введите высоту прямоугольника: "))
    if w <= 0 or h <= 0:
        print("ошибка: стороны должны быть больше нуля")
        return None
    return w, h


#№ БЛОК ФУНКЦИЙ ВЫВОДА РЕЗУЛЬТАТОВ


def show_result(figure_name, area):
    "выводит результат вычислений на экран"
    print("\n" + "="*30)
    print(f"Фигура: {figure_name}")
    print(f"Площадь равна: {round(area, 2)}")
    print("="*30 + "\n")


## ГЛАВНОЕ МЕНЮ (УПРАВЛЕНИЕ)


def main_menu():
    "работа интерактивного меню"
    while True:
        print("ГЕОМЕТРИЧЕСКИЙ КАЛЬКУЛЯТОР")
        print("1. Площадь круга")
        print("2. Площадь треугольника")
        print("3. Площадь прямоугольника")
        print("0. Выход из программы")
        
        choice = input("Выберите пункт меню: ")
        
        if choice == "1":
            radius = input_circle()
            if radius is not None:
                area = calculate_circle_area(radius)
                show_result("Круг", area)
                
        elif choice == "2":
            triangle_data = input_triangle()
            if triangle_data is not None:
                a, b, c = triangle_data
                area = calculate_triangle_area(a, b, c)
                show_result("Треугольник", area)
                
        elif choice == "3":
            rectangle_data = input_rectangle()
            if rectangle_data is not None:
                w, h = rectangle_data
                area = calculate_rectangle_area(w, h)
                show_result("Прямоугольник", area)
                
        elif choice == "0":
            print("Программа завершена")
            break
        else:
            print("\nНеверный пункт меню\n")

# запуск программы
main_menu()