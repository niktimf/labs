from pprint import pprint


# Задание 1

# Выводим приветственное сообщение на экран
print('Hello, world!')
# Спрашиваем имя пользователя и ждем ввода
print('What is your name?')
myName = input()  # Сохраняем введенное имя в переменную myName
# Выводим сообщение с использованием введенного имени
print('It is good to meet you, ' + myName)
# Сообщаем пользователю длину его имени
print('The length of your name is:')
print(len(myName))  # Функция len() возвращает количество символов в имени
# Запрашиваем возраст пользователя
print('What is your age?')
myAge = input()  # Сохраняем введенный возраст в переменную myAge
# Рассчитываем и выводим возраст пользователя через год
print('You will be ' + str(int(myAge) + 1) + ' in a year.')


# Задание 2

x = 2  # Начальное значение переменной x
results = [(x, type(x).__name__)]  # Сохраняем начальное значение x и его тип в список results

# Прибавляем 3 к x и сохраняем результат
x += 3
results.append((x, type(x).__name__))  # Добавляем новое значение и его тип в список

# Делим x+1 на 2 и сохраняем результат
x = (x + 1) / 2
results.append((x, type(x).__name__))  # Добавляем новое значение и его тип в список

# Прибавляем к текущему значению x 1/2
x = x + 1 / 2
results.append((x, type(x).__name__))  # Добавляем новое значение и его тип в список

# Проверяем, меньше ли x 5, и сохраняем результат (True или False)
x = x < 5
results.append((x, type(x).__name__))  # Добавляем новое значение (булево) и его тип в список

# Преобразуем x из булева типа в строковый
x = str(x)
results.append((x, type(x).__name__))  # Добавляем новое строковое значение и его тип в список

pprint(results)  # Красиво выводим список результатов


# Задание 3

def mean_average(numbers: list, precision: int) -> float:
    """
    Функция для вычисления среднего арифметического списка чисел с заданной точностью.
    :param numbers: список чисел
    :param precision: точность (количество знаков после запятой)
    :return: среднее значение с заданной точностью
    """
    return round(sum(numbers) / len(numbers), precision)  # Возвращаем округленное среднее значение


numbers = [1, 2, 3, 4, 5]  # Список чисел
precision = 5  # Точность вычисления
mean_average = mean_average(numbers, precision)  # Вызываем функцию и сохраняем результат
# Выводим результат
print(f'Среднее значение этих {len(numbers)} чисел равно {mean_average} и результат работы с точностью до {precision} знака после запятой')


# Задание 4
# 1).Вставить слово "Привет" в пустой строке перед определением переменной v0.
# 2).Удалить знак # перед комментарием "Начальная скорость".
# 3).Удалить знак = в задании переменной v0.
# 4).Заменить слово print на pint.
# 5).Заменить строку print(y) на print(x).
# 6).Заменить выражение g = 9.80665 и t = 0.1 на g: int = 9.80665 и t: int = 0.1, а потом на g = int(9.80665) и t = int(0.1).

# Программа для вычисления положения мяча при вертикальном движении
v0 = 50  # Начальная скорость (м / с)
g = 9.80665  # Ускорение свободного падения (м / с^2)
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

# Определение и выполнение операции перевода в зависимости от введенных данных
match (unit_from, unit_to):
    # Случай когда пользователь вводит сначала км, а потом мили
    case ("км", "мили"):
        result = convert_km_to_miles(amount)  # Вызов функции перевода км в мили
        print(f"{amount} км равно {result} миль.")  # Вывод результата
    # Случай когда пользователь вводит сначала мили, а потом км
    case ("мили", "км"):
        result = convert_miles_to_km(amount)  # Вызов функции перевода миль в км
        print(f"{amount} миль равно {result} км.")  # Вывод результата
    # Случай когда пользователь вводит неподдерживаемую единицу измерения
    case _:
        # Сообщение об ошибке, если введены неподдерживаемые единицы измерения
        print("Некорректный ввод единиц измерения.")

# Этот блок кода позволяет пользователю ввести количество единиц и выбрать,
# в какую единицу измерения он хочет это перевести (км в мили или мили в км).
# Затем программа использует соответствующую функцию для перевода и выводит результат.
