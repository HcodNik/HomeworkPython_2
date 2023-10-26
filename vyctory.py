"""ПРОГРАММА ВИКТОРИНА"""
yearPushkin = int(input("Укажите год рождения Александра Пушкина: ")) # 1799
yearEinstein = int(input("Укажите год рождения Альберта Эйнштейна: ")) # 1879
yearTesla = int(input("Укажите год рождения Николы Тесла: ")) # 1856
yearJobs = int(input("Укажите год рождения Стива Джобса: ")) # 1955
yearTuring = int(input("Укажите год рождения Алана Тьюринга: ")) # 1912
catch0 = 0 # счётчик правильных ответов
catch1 = 0 # счётчик неправильных ответов

if yearPushkin == 1799:
    catch0 += 1
else:
    catch1 += 1
if yearEinstein == 1879:
    catch0 += 1
else:
    catch1 += 1
if yearTesla == 1856:
    catch0 += 1
else:
    catch1 += 1
if yearJobs == 1955:
    catch0 += 1
else:
    catch1 += 1
if yearTuring == 1912:
    catch0 += 1
else:
    catch1 += 1

print("Кол-во правильных ответов:", catch0)
print("Кол-во ошибок:", catch1)
print("Процент правильных ответов:", catch0*100/5)
print("Процент неправильных ответов:", catch1*100/5)