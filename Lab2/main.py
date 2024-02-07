# Задание 1

day = int(input("Введите день рождения: "))
month = input("Введите месяц рождения: ").lower()


def zodiac_sign(day, month):
    if (month == "март" and day >= 21) or (month == "апрель" and day <= 19):
        return "Овен"
    elif (month == "апрель" and day >= 20) or (month == "май" and day <= 20):
        return "Телец"
    elif (month == "май" and day >= 21) or (month == "июнь" and day <= 21):
        return "Близнецы"
    elif (month == "июнь" and day >= 22) or (month == "июль" and day <= 22):
        return "Рак"
    elif (month == "июль" and day >= 23) or (month == "август" and day <= 22):
        return "Лев"
    elif (month == "август" and day >= 23) or (month == "сентябрь" and day <= 22):
        return "Дева"
    elif (month == "сентябрь" and day >= 23) or (month == "октябрь" and day <= 23):
        return "Весы"
    elif (month == "октябрь" and day >= 24) or (month == "ноябрь" and day <= 22):
        return "Скорпион"
    elif (month == "ноябрь" and day >= 23) or (month == "декабрь" and day <= 21):
        return "Стрелец"
    elif (month == "декабрь" and day >= 22) or (month == "январь" and day <= 20):
        return "Козерог"
    elif (month == "январь" and day >= 21) or (month == "февраль" and day <= 19):
        return "Водолей"
    elif (month == "февраль" and day >= 20) or (month == "март" and day <= 20):
        return "Рыбы"
    else:
        return "Неизвестный знак зодиака"


print(f"Ваш знак зодиака: {zodiac_sign(day, month)}")


# Задание 2
def is_symmetric(number):
    str_number = str(number).zfill(4)
    return str_number == str_number[::-1]


number = input("Введите четырехзначное число: ")
print(True if is_symmetric(number) else False)


# Задание 3
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


year = int(input("Введите год: "))
print("YES" if is_leap_year(year) else "NO")


# Задание 4
def correct_form(n):
    if 10 < n % 100 < 15:
        return "коров"
    elif n % 10 == 1:
        return "корова"
    elif 1 < n % 10 < 5:
        return "коровы"
    else:
        return "коров"


n = int(input("Введите число коров: "))
print(f"На лугу пасется {n} {correct_form(n)}")


# Задание 5

def min_divisor_for(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i


n = int(input("Введите число: "))
print(min_divisor_for(n))


def min_divisor_while(n):
    i = 2
    while n % i != 0:
        i += 1
    return i


n = int(input("Введите число: "))
print(min_divisor_while(n))
