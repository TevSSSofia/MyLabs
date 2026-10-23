## ввод строки
text = input("Введите строку текста: ")

# пустота строки
if text == "":
    print("Ошибка: строка пустая!")
else:


## обработка спецсимволов и знаков препинания

# Создаем строку со всеми символами, которые нужно удалить
    specials = ".,!?;:-()\"'*/\\@#$%^&_+=<>[]{}|"
    
# заменяем каждый спецсимвол на пустоту
    cleaned_text = ""
    for char in text:
        if char not in specials:
            cleaned_text += char
        else:
            cleaned_text += " " # заменяем спецсимвол на пробел

# разбиваем строку на слова    
    words = cleaned_text.split()
# Если после удаления спецсимволов слов не осталось (ввели только знаки)
    if len(words) == 0:
        print("Ошибка: строка содержит только спецсимволы!")

# считаем количество слов (длина списка)
    words_count = len(words)
        
# считаем колво букв в словах 
    max_len = len(words[0])
    min_len = len(words[0])
    
# перебираем все слова в цикле
    for word in words:
        if len(word) > max_len:
            max_len = len(word)
        if len(word) < min_len:
            min_len = len(word)

# если в тексте есть слова с одинаково коротким или длинным колвом букв создаем их список
    all_longest = []
    all_shortest = []

#собираем все слова 
for word in words:
# приводим к нижнему регистру, чтобы слова "Слово" и "слово" считались одинаковыми
            word_lower = word.lower() 
            
            if len(word) == max_len:
                if word_lower not in [w.lower() for w in all_longest]:
                    all_longest.append(word)
                    
            if len(word) == min_len:
                if word_lower not in [w.lower() for w in all_shortest]:
                    all_shortest.append(word)            
# вывод результатов
print("\nРезультаты")
print("Всего слов в строке:", len(words))
print("Самые длинные слова (длина {}):".format(max_len), all_longest)
print("Самые короткие слова (длина {}):".format(min_len), all_shortest)