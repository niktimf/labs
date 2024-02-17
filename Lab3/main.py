from functools import reduce
import polars as pl


# Задание 1

def calculate_pi_polars(n: int) -> pl.DataFrame:
    """
    Функция для вычисления числа π по формулам Мадхавы-Лейбница и Валлиса с использованием Polars
    :param n: число итераций
    :return: DataFrame(это двумерная структура данных,
    представляющая собой таблицу с метками для строк и столбцов.
    Каждый столбец в DataFrame является объектом типа Series.
    Вместе они формируют двумерную таблицу с общим индексом.
    В DataFrame присутствуют две оси индексации: index для строк и columns для столбцов)
    с вычисленными значениями
    """

    # Создаем DataFrame с итерациями
    df = pl.DataFrame({"Итерация": range(1, n + 1)})

    # Вычисляем значения по формуле Мадхавы-Лейбница
    madhava_leibniz = [4 * sum((-1) ** i / (2 * i + 1) for i in range(k)) for k in range(1, n + 1)]

    # Вычисляем значения по формуле Валлиса
    wallis = [2 * reduce(lambda acc, x: acc * (4 * x ** 2 / (4 * x ** 2 - 1)), range(1, k + 1), 1) for k in range(1, n + 1)]

    # Добавляем вычисленные столбцы в DataFrame
    df = df.with_columns([
        pl.Series("Мадхава-Лейбниц", madhava_leibniz),
        pl.Series("Валлис", wallis)
    ])

    return df


df_pi_polars = calculate_pi_polars(10)
print(df_pi_polars)


# Задание 2

def find_pythagorean_triples(n: int) -> list:
    """
    Функция для нахождения пифагоровых троек в заданном диапазоне.
    :param n: максимальное значение диапазона для поиска
    :return: список троек
    """
    # Генерация всех возможных комбинаций троек и фильтрация по условию Пифагора
    return [
        (x, y, z)
        # Цикл для x (от 1 до n -1)
        # x начинается с 1, потому что в пифагоровой тройке не может быть числа меньше 1.
        # n−1, потому что x является наименьшим числом в тройке, и для того чтобы оставить место для y и z (которые должны быть больше x),
        # мы не рассматриваем последнее значение n. Это обеспечивает, что у y и z будет возможность быть выбранными в диапазоне больше x.

        for x in range(1, n - 1)
        # Цикл для y (от x + 1 до n)
        # y начинается с x + 1, чтобы гарантировать, что y больше x. Это следует из определения пифагоровых троек,
        # где каждое следующее число больше предыдущего.
        # y идет до n, что дает y максимально возможное значение в данном диапазоне,
        # оставаясь при этом строго меньше z, так как z начинается с y + 1

        for y in range(x + 1, n)
        # Цикл для z (от y + 1 до n)
        # z начинается с y + 1, что обеспечивает его строгое превосходство над y и, соответственно, над x.
        # Это необходимо для соответствия определению пифагоровых троек.
        # z идет до n + 1, потому что в условии x^2 + y^2 = z^2, z является наибольшим числом,
        # и его максимальное значение может равняться n.
        # Включение n + 1 в диапазон необходимо, так как функция range в Python исключает последнее значение.
        for z in range(y + 1, n + 1)

        # Проверка условия Пифагора
        if x ** 2 + y ** 2 == z ** 2
    ]


# Выводим пифагоровы тройки до 30
print(f'Пифагоровы тройки: {find_pythagorean_triples(30)}')


# Задание 3
def format_verse(n: int) -> str:
    """
    Функция для формирования куплета песни в зависимости от количества бутылок.
    :param n: количество бутылок
    :return: строка куплета
    """
    next_n = n - 1  # Следующее количество бутылок
    # Первая часть строки, которая изменяется в зависимости от количества бутылок
    bottles = lambda x: f"{x} green bottle{'s' if x > 1 else ''} hanging on the wall"
    # Формирование строки куплета
    verse = f"{bottles(n)},\n" * 2 + \
            "And if one green bottle should accidentally fall,\n" + \
            f"There’ll be {bottles(next_n)}.\n"
    return verse if n > 1 else verse.replace("And if", "If that")  # Заменяем начало последней строки для 1 бутылки


# Создание и вывод полного текста песни, генерируя куплеты от 10 до 1
song_text = "\n".join(map(format_verse, range(10, 0, -1)))
print(song_text)


# Задание 4
def fill_top(matrix: list, top: int, left: int, right: int, value: int) -> int:
    """
    Функция для заполнения верхней строки матрицы
    :param matrix: матрица
    :param top: верхняя граница
    :param left: левая граница
    :param right: правая граница
    :param value: значение
    :return: обновленное значение для следующего шага
    """
    # Проходимся по элементам верхней строки от левого до правого края
    for i in range(left, right + 1):
        matrix[top][i] = value  # Присваиваем значение
        value += 1  # Увеличиваем значение на 1 для следующего элемента
    return value


def fill_right(matrix: list, right: int, top: int, bottom: int, value: int) -> int:
    """
    Функция для заполнения правой стороны матрицы
    :param matrix: матрица
    :param right: правая граница
    :param top: верхняя граница
    :param bottom: нижняя граница
    :param value: значение
    :return: обновленное значение для следующего шага
    """
    # Проходимся по элементам правой колонки сверху вниз
    for i in range(top, bottom + 1):
        matrix[i][right] = value  # Присваиваем значение
        value += 1  # Увеличиваем значение на 1 для следующего элемента
    return value


def fill_bottom(matrix: list, bottom: int, left: int, right: int, value: int) -> int:
    """
    Функция для заполнения нижней стороны матрицы
    :param matrix: матрица
    :param bottom: нижняя граница
    :param left: левая граница
    :param right: правая граница
    :param value: значение
    :return: обновленное значение для следующего шага
    """
    # Проходимся по элементам нижней строки справа налево
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = value  # Присваиваем значение
        value += 1  # Увеличиваем значение на 1 для следующего элемента
    return value


def fill_left(matrix: list, left: int, top: int, bottom: int, value: int) -> int:
    """
    Функция для заполнения левой стороны матрицы
    :param matrix: матрица
    :param left: левая граница
    :param top: верхняя граница
    :param bottom: нижняя граница
    :param value: значение
    :return: обновленное значение для следующего шага
    """
    # Проходимся по элементам левой колонки снизу вверх
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = value  # Присваиваем значение
        value += 1  # Увеличиваем значение на 1 для следующего элемента
    return value


def fill_matrix_spirally(n: int) -> list:
    """
    Функция для заполнения матрицы спиралью
    :param n: размерность матрицы
    :return: матрица заполненная спиралью
    """
    # Инициализируем матрицу нулями
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    # Начальные параметры для заполнения
    value, left, right, top, bottom = 1, 0, n - 1, 0, n - 1

    # Цикл продолжается, пока не заполним всю матрицу
    while value <= n * n:
        value = fill_top(matrix, top, left, right, value)  # Заполняем верх
        top += 1  # Сдвигаем верхнюю границу вниз
        value = fill_right(matrix, right, top, bottom, value)  # Заполняем право
        right -= 1  # Сдвигаем правую границу влево
        value = fill_bottom(matrix, bottom, left, right, value)  # Заполняем низ
        bottom -= 1  # Сдвигаем нижнюю границу вверх
        value = fill_left(matrix, left, top, bottom, value)  # Заполняем лево
        left += 1  # Сдвигаем левую границу вправо

    return matrix


# Демонстрация работы функции заполнения матрицы по спирали
matrix_size = 5
spiral_matrix = fill_matrix_spirally(matrix_size)
for row in spiral_matrix:
    print(row)  # Вывод каждой строки заполненной матрицы


# Задание 5


def create_and_fill_matrix(n: int) -> list:
    """
    Функция для создания и заполнения квадратной матрицы порядка n(размера n)
    Создает квадратную матрицу порядка n и заполняет ее значениями.
    Значения в матрице идут по порядку от 1 до n^2, построчно.
    :param n: Размерность матрицы.
    :return: Заполненная матрица.
    """
    # Создаем матрицу с помощью вложенных списков(список списков)
    # i * n + j + 1 гарантирует последовательное заполнение значений в матрице
    matrix = [
        [i * n + j + 1 for j in range(n)]
        for i in range(n)
    ]
    return matrix



def swap_diagonals(matrix: list) -> list:
    """
    Функция для обмена диагоналей в квадратной матрице
    Меняет местами элементы главной и побочной диагонали в квадратной матрице.
    :param matrix: Квадратная матрица для модификации.
    :return: Матрица с переставленными диагоналями.
    """
    n = len(matrix)  # Получаем размер матрицы
    for i in range(n):
        # Обмен значениями между главной и побочной диагоналями
        # matrix[i][i] - элемент главной диагонали
        # matrix[i][n - 1 - i] - элемент побочной диагонали
        matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]
    return matrix


# Создание и заполнение матрицы порядка 5
n = 5
matrix = create_and_fill_matrix(n)

# Вывод исходной матрицы
print("\nИсходная матрица:")
for row in matrix:
    print(row)

# Применение функции обмена диагоналей
swapped_matrix = swap_diagonals(matrix)

# Вывод модифицированной матрицы
print("\nМатрица после обмена диагоналей:")
for row in swapped_matrix:
    print(row)
