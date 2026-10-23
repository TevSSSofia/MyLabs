import unittest

## класс для расчетов с датами
class DateCalculator:
    def __init__(self, day=1, month=1, year=2026):
        # обработка исключений: проверяем корректность типов данных
        if not isinstance(day, int) or not isinstance(month, int) or not isinstance(year, int):
            raise TypeError("дата должна состоять только из целых чисел")
            
        # обработка исключений: проверяем логику дат (календарь по 30 дней)
        if day < 1 or day > 30 or month < 1 or month > 12 or year < 1:
            raise ValueError("некорректное значение дня, месяца или года")

        self.day = day
        self.month = month
        self.year = year

## метод для прибавления дней
    def add_days(self, days_to_add):
        if not isinstance(days_to_add, int):
            raise TypeError("количество дней должно быть целым числом")
        if days_to_add < 0:
            raise ValueError("нельзя прибавить отрицательное количество дней")

        self.day += days_to_add
        while self.day > 30:
            self.day -= 30
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
        return self.day, self.month, self.year

## метод для расчета разницы в днях между двумя датами
    def days_between(self, other_date):
        if not isinstance(other_date, DateCalculator):
            raise TypeError("сравнивать можно только с другим объектом DateCalculator")

        total_days1 = self.year * 360 + self.month * 30 + self.day
        total_days2 = other_date.year * 360 + other_date.month * 30 + other_date.day
        return abs(total_days1 - total_days2)


## блок из 10 элементарных юнит тестов
class TestDateCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = DateCalculator(1, 1, 2026)

    def test_start_day(self):
        self.assertEqual(self.calc.day, 1)

    def test_start_month(self):
        self.assertEqual(self.calc.month, 1)

    def test_start_year(self):
        self.assertEqual(self.calc.year, 2026)

    def test_add_few_days(self):
        res = self.calc.add_days(5)
        self.assertEqual(res, (6, 1, 2026))

    def test_add_days_next_month(self):
        res = self.calc.add_days(35)
        self.assertEqual(res, (6, 2, 2026))

    def test_add_days_next_year(self):
        res = self.calc.add_days(365)
        self.assertEqual(res, (6, 1, 2027))

    def test_diff_same_date(self):
        date2 = DateCalculator(1, 1, 2026)
        self.assertEqual(self.calc.days_between(date2), 0)

    def test_exception_type_error(self):
        with self.assertRaises(TypeError):
            DateCalculator("1", 1, 2026)

    def test_exception_value_error(self):
        with self.assertRaises(ValueError):
            DateCalculator(40, 1, 2026)

    def test_exception_negative_days(self):
        with self.assertRaises(ValueError):
            self.calc.add_days(-10)


## функция для интерактивного меню и ввода с клавиатуры
def run_menu():
    print("калькулятор дат (в месяце строго 30 дней)")
    try:
        # запрашиваем базовую дату
        d = int(input("введите день: "))
        m = int(input("введите месяц: "))
        y = int(input("введите год: "))
        
        # создаем объект (может вызвать ошибку валдиации)
        user_date = DateCalculator(d, m, y)
        
        print("\nвыберите действие:")
        print("1. прибавить дни к этой дате")
        print("2. посчитать разницу с другой датой")
        choice = input("ваш выбор: ")
        
        if choice == "1":
            days = int(input("сколько дней прибавить: "))
            res_d, res_m, res_y = user_date.add_days(days)
            print(f"новая дата: {res_d}.{res_m}.{res_y}")
            
        elif choice == "2":
            print("\nвведите вторую дату:")
            d2 = int(input("введите день: "))
            m2 = int(input("введите месяц: "))
            y2 = int(input("введите год: "))
            
            second_date = DateCalculator(d2, m2, y2)
            diff = user_date.days_between(second_date)
            print(f"разница между датами: {diff} дней")
        else:
            print("ошибка: неверный пункт меню")
            
    except ValueError as e:
        print(f"ошибка ввода: {e}")
    except TypeError as e:
        print(f"ошибка типа данных: {e}")


## главный блок запуска программы
if __name__ == '__main__':
    # сначала автоматически запускаются тесты для отчета преподавателю
    print("запуск юнит-тестов модуля:")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDateCalculator)
    runner = unittest.TextTestRunner(verbosity=2)
    test_result = runner.run(suite)
    
    # если тесты прошли успешно, открывается ввод с клавиатуры
    if test_result.wasSuccessful():
        print("\nвсе тесты пройдены успешно!\n")
        run_menu()
