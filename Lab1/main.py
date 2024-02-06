from pprint import pprint

# Задание 1

print('Hello, world!')
print('What is your name?')
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


# Задание 2

x = 2
results = [(x, type(x).__name__)]

# Прибавляем 3 к x и присваиваем это значение x
x += 3
results.append((x, type(x).__name__))

# Вычисляем (x+1)/2 и присваиваем это значение x
x = (x + 1) / 2
results.append((x, type(x).__name__))

# Вычисляем x + 1/2 и присваиваем это значение x
x = x + 1 / 2
results.append((x, type(x).__name__))

# Присваиваем x результат выражения x < 5
x = x < 5
results.append((x, type(x).__name__))

# Изменяем тип x в символьный и присваиваем результат переменной x
x = str(x)
results.append((x, type(x).__name__))

pprint(results)


# Задание 3

def mean_average(numbers: list, precision: int) -> float:
    return round(sum(numbers) / len(numbers), precision)


numbers = [1, 2, 3, 4, 5]
precision = 5
mean_average = mean_average(numbers, precision)
print(f'Среднее значение этих {len(numbers)} чисел равно {mean_average} и результат работы с точностью до {precision} знака после запятой')


# Задание 4
# 1).Вставить слово "Привет" в пустой строке перед определением переменной v0.
# 2).Удалить знак # перед комментарием "Начальная скорость".
# 3).Удалить знак = в задании переменной v0.
# 4).Заменить слово print на pint.
# 5).Заменить строку print(y) на print(x).
# 6).Заменить выражение g = 9.80665 и t = 0.1 на g: int = 9.80665 и t: int = 0.1, а потом на g = int(9.80665) и t = int(0.1).

# Программа для вычисления положения мяча при вертикальном движении
v0 = 50  # Начальная скорость (м/с)
g = 9.80665  # Ускорение свободного падения (м/с^2)
t = 0.6  # Время (с)
y = v0 * t - 1 / 2 * g * t ** 2  # (м)
print(y)
print('{:<30} {:.5e} м/c'.format('Начальная скорость', v0))


# error 1 ---> SyntaxError: invalid syntax (Вставьте слово "Привет" в пустой строке перед определением переменной v0.)
# error 2 ---> SyntaxError: invalid syntax (Удалите знак # перед комментарием "Начальная скорость")
# error 3 ---> SyntaxError: invalid syntax (Удалите знак = в задании переменной v0)
# error 4 ---> NameError: name 'pint' is not defined. Did you mean: 'print'? (Замените слово print на pint)
# error 5 ---> Нет ошибок (Замените строку print(y) на print(x))
# error 6 ---> Нет ошибок, так как в 1 случае мы указали тип переменной хоть и неправильный,
# и получили Warning: Expected type 'int', got 'float' instead,
# а во 2 случае мы преобразовали тип переменной в int (Замените выражение g = 9.80665 и t = 0.1 на g: int = 9.80665 и t: int = 0.1,
# а потом на g = int(9.80665) и t = int(0.1))


# Задание 5
# Перевод километров в мили и наоборот с выводом результата
def convert_km_to_miles(km):
    """
    Функция для перевода километров в мили.
    :param km: число километров
    :return: число миль
    """
    return km * 0.621371


def convert_miles_to_km(miles):
    """
    Функция для перевода миль в километры.
    :param miles: число миль
    :return: число километров
    """
    return miles / 0.621371


# Запрос ввода от пользователя
amount = float(input("Введите количество единиц для перевода: "))
unit_from = input("Введите единицу измерения (км или мили): ")
unit_to = input("Введите целевую единицу измерения (км или мили): ")

match (unit_from, unit_to):
    case ("км", "мили"):
        result = convert_km_to_miles(amount)
        print(f"{amount} км равно {result} миль.")
    case ("мили", "км"):
        result = convert_miles_to_km(amount)
        print(f"{amount} миль равно {result} км.")
    case _:
        print("Некорректный ввод единиц измерения.")
