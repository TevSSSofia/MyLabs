## заполнение массива из 10 чисел
print("ВВОД МАССИВА")
list = []

# запрашиваем 10 чисел и добавляем их в список
for i in range(10):
    num = float(input(f"Введите элемент массива с индексом [{i}]: "))
    list.append(num)

# Выводим исходный массив для наглядности
print("\nИсходный массив:", list)


## поиск статистических данных

# вводим начальные данные

# за min и max изначально берем самый первый элемент массива по индексу 0 
total_sum = 0
min_val = list[0]
max_val = list[0]
min_index = 0
max_index = 0


## проходим циклом по массиву
for i in range(10):
    current_element = list[i]
    
# считаем сумму
    total_sum += current_element
    
# ищем минимальный элемент и его индекс
    if current_element < min_val:
        min_val = current_element
        min_index = i
        
# ищем максимальный элемент и его индекс
    if current_element > max_val:
        max_val = current_element
        max_index = i


## считаем среднее арифметическое
average = total_sum / 10


## вывод результатов расчетов
print("\nРЕЗУЛЬТАТЫ РАСЧЕТОВ")
print(f"Сумма всех элементов: {round(total_sum, 2)}")
print(f"Среднее арифметическое: {round(average, 2)}")
print(f"Минимальный элемент: {min_val} (его индекс: {min_index})")
print(f"Максимальный элемент: {max_val} (его индекс: {max_index})")