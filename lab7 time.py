class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        "конструктор класса с проверкой корректности времени"
        # инкапсуляция: приватные поля, скрытые от прямого доступа
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        
        # Устанавливаем значения через свойства, чтобы сработала валидация
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # свойства
    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        if 0 <= value < 24:
            self.__hours = value
        else:
            self.__hours = 0  # Сброс в дефолт при некорректном вводе

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        if 0 <= value < 60:
            self.__minutes = value
        else:
            self.__minutes = 0

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        if 0 <= value < 60:
            self.__seconds = value
        else:
            self.__seconds = 0

    # ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ (ИЗБЕГАЕМ ДУБЛИРОВАНИЯ)
    def to_seconds(self):
        "Переводит текущее время в общее количество секунд"
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    @staticmethod
    def from_seconds(total_seconds):
        "создает новый объект Time из общего количества секунд"
        # Обработка переполнения суток (остаток от деления на секунды в 24 часах)
        total_seconds = total_seconds % 86400
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        return Time(h, m, s)

    # ОСНОВНЫЕ МЕТОДЫ ЗАДАНИЯ
    def add(self, other):
        """Сложение двух промежутков времени"""
        total = self.to_seconds() + other.to_seconds()
        return Time.from_seconds(total)

    def difference(self, other):
        """Разница между двумя промежутками времени (по модулю)"""
        diff = abs(self.to_seconds() - other.to_seconds())
        return Time.from_seconds(diff)

    def compare(self, other):
        "Сравнение времени: возвращает 1 если self >, -1 если self <, 0 если =="
        t1 = self.to_seconds()
        t2 = other.to_seconds()
        if t1 > t2:
            return 1
        elif t1 < t2:
            return -1
        else:
            return 0

    def display(self):
        """Вывод времени в формате ЧЧ:ММ:СС"""
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"


# ДЕМОНСТРАЦИЯ РАБОТЫ
if __name__ == "__main__":
    print("создание объектов времени")
    t1 = Time(10, 45, 30)
    t2 = Time(2, 20, 45)
    
    print("Время 1:", t1.display())
    print("Время 2:", t2.display())

    print("\nвычисление операций")
    t_sum = t1.add(t2)
    print("Результат сложения:", t_sum.display())

    t_diff = t1.difference(t2)
    print("Разница времени:", t_diff.display())

    print("\nсравнение времени")
    cmp = t1.compare(t2)
    if cmp == 1:
        print("время 1 больше, чем Время 2")
    elif cmp == -1:
        print("время 1 меньше, чем Время 2")
    else:
        print("Время одинаковое")
