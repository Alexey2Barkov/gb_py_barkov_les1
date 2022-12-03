# Урок 2. Задание 4.
text = input("Введите слова через пробел : ")
t = text.split()
for x, y in enumerate(t, start=1):
    if len(y) > 11:
        y = y[:10]
        print(x, y)
    else:
        print(x, y)
