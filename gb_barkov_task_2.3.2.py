# Урок 2. Задание 3.2
month = int(input("Введите номер месяца от 1 до 12: "))
seasons = {1: "зима", 2: "весна", 3: "лето", 4: "осень"}
months_dict = {12: seasons.get(1), 1: seasons.get(1), 2: seasons.get(1),
               3: seasons.get(2), 4: seasons.get(2), 5: seasons.get(2),
               6: seasons.get(3), 7: seasons.get(3), 8: seasons.get(3),
               9: seasons.get(4), 10: seasons.get(4), 11: seasons.get(4)}
value = months_dict[month] if month in months_dict else print(f"НЕТ ТАКОГО МЕСЯЦА")
print(f"Ваш месяц относится к времени года: {value}")
