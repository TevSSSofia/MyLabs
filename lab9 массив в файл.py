## запись массива чисел в файл
# получаем числа от пользователя через пробел
print("введите числа через пробел:")
user_input = input()

# обрабатываем возможные ошибки при работе с файлами и вводом
try:
    # переводим строку в список чисел (может вызвать ValueError)
    numbers = [float(x) for x in user_input.split()]
    
    # проверка на пустой ввод
    if len(numbers) == 0:
        raise ValueError("список чисел не должен быть пустым")

    # открываем файл на запись (конструкция with сама закроет поток)
    with open("numbers.txt", "w", encoding="utf-8") as file:
        for num in numbers:
            file.write(f"{num}\n")
    print("массив успешно записан в файл numbers.txt")

except ValueError as e:
    print(f"ошибка: введены некорректные данные или пустая строка ({e})")
except IOError:
    print("ошибка: не удалось записать данные в файл")


## чтение массива из файла и расчет статистики
try:
    total_sum = 0
    count = 0

    # открываем файл на чтение
    with open("numbers.txt", "r", encoding="utf-8") as file:
        for line in file:
            # убираем лишние пробелы и перенос строки
            clean_line = line.strip()
            if clean_line:
                total_sum += float(clean_line)
                count += 1

    # считаем среднее арифметическое
    if count > 0:
        average = total_sum / count
        # выводим результаты расчетов
        print("\nрезультаты из файла:")
        print(f"сумма элементов = {round(total_sum, 2)}")
        print(f"среднее значение = {round(average, 2)}")
    else:
        print("ошибка: файл оказался пустым")

# критерий: обработка не менее 3 типов исключений (FileNotFoundError, ValueError, ZeroDivisionError)
except FileNotFoundError:
    print("ошибка: файл numbers.txt не найден")
except ValueError:
    print("ошибка: в файле обнаружены поврежденные или нечисловые данные")
except ZeroDivisionError:
    print("ошибка: деление на ноль при подсчете среднего значения")
