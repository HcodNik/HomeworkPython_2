yearPushkin = int(input("Укажите год рождения А.С. Пушкина: "))
dayPushkin = 0

if yearPushkin == 1799:
    print("Верно. Тот самый год!")
    dayPushkin = int(input("Укажите день рождения А.С. Пушкина: "))
    if dayPushkin == 6:
        print("Верно!")
    else:
        print("Неверный день рождения!")
else:
    print("Неверный год!")