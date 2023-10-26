catch = 0 # заводим промежуточную переменную

while catch == 0:
    yearPushkin = int(input("Укажите год рождения А.С. Пушкина: "))

    if yearPushkin == 1799:
        catch = 1
        print("Верно!")
    else:
        print("Вы ошиблись. Неверно!")
