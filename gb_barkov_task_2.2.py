# Урок 2. Задание 2.
s = int(input("Укажите количество элементов списка: "))
lst1 = []
for x in range(s):
    lst1.append(input(f"Элемент {x + 1}: "))
print(f"Исходный список:\n{lst1}")
for y in range(0, (len(lst1) - 1), 2):
    lst1[y], lst1[y + 1] = lst1[y + 1], lst1[y]
print(f"Обработанный список:\n{lst1}")
