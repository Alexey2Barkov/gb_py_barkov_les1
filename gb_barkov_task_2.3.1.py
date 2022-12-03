# Урок 2. Задание 3.1
month = int(input("Введите номер месяца от 1 до 12: "))
list1 = ["зима", "весна", "лето", "осень"]
while True:
    if month > 12 or month <= 0:
        print(f"НЕТ ТАКОГО МЕСЯЦА")
        month = int(input("Введите номер месяца от 1 до 12: "))
        continue
    list1 = ["зима", "весна", "лето", "осень"]
    if month == 12 or (month >= 1 and month < 3):
        print(f"Ваш месяц относится к времени года: {list1[0]}")
        break
    elif month >= 3 and month < 6:
        print(f"Ваш месяц относится к времени года: {list1[1]}")
        break
    elif month >= 6 and month < 9:
        print(f"Ваш месяц относится к времени года: {list1[2]}")
        break
    elif month >= 9 and month < 12:
        print(f"Ваш месяц относится к времени года: {list1[3]}")
        break
