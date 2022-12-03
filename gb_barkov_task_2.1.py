# Урок 2. Задание 1.
type_list = [True, 5, 1 / 2, [3, 4], (5, 6), "Строка", {"Словарь": "Англо-русский", "Год": "Високосный"}]
for i in range(len(type_list)):
    print(f"Проверка: {type(type_list[i])}")
