# Урок 2. Задание 6.
x = int(input("Сколько новых позиций нужно добавить в БД: "))
bd = "Название", "Цена", "Количество", "Ед.изм"
product, name, cost, qy, ei = [], [], [], [], []
for i in range(x):
    print(f"Позиция {i + 1} :")
    namei, pricei, qyi, eii = input("\tНазвание : "), input("\tЦена  : "), input("\tКол-во : "), \
                              input("\tЕд.изм : ")
    product_up = (i + 1, {bd[0]: namei, bd[1]: pricei, bd[2]: qyi, bd[3]: eii})
    product.append(product_up)
    name.append(product[i][1].get(bd[0]))
    cost.append(product[i][1].get(bd[1]))
    qy.append(product[i][1].get(bd[2]))
    ei.append(product[i][1].get(bd[3]))
analytics = {bd[0]: name, bd[1]: cost, bd[2]: qy, bd[3]: ei}
print(f"Статистика \n{analytics}")
