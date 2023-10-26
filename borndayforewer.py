catch = 0 # заводим промежуточную переменную

while catch ==0:
    yearPushkin = int(input("Укажите год рождения А.С. Пушкина: "))
    dayPushkin = 0

    if yearPushkin == 1799:
        catch = 1
        print("Верно. Тот самый год!")
        while catch == 1:
            dayPushkin = int(input("Укажите день рождения А.С. Пушкина: "))
            if dayPushkin == 6:
                catch = 2
                print("Верно! Тот самый день!")
            else:
                print("Неверный день рождения!")
    else:
        print("Неверный год!")