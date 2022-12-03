# Урок 2. Задание 5.
rtlst = [7, 5, 3, 3, 2]
x = int(input("Добавьте число в рейтинг "))
if x in rtlst:
    i = rtlst.index(x)
    while (i + 1) <= (len(rtlst) - 1) and (rtlst[i] == rtlst[i + 1]):
        i += 1
    rtlst.insert(i, x)
    print(f"Новый рейтинг {rtlst}")
else:
    if x <= rtlst[-1]:
        rtlst.append(x)
        print(f"Новый рейтинг {rtlst}")
    else:
        rtlst.insert(0, x)
        print(f"Новый рейтинг {rtlst}")
