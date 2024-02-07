from functools import reduce
import polars as pl


# Задание 1
# Функция для вычисления следующего члена ряда по формуле Мадхавы-Лейбница
def next_madhava_leibniz_term(i):
    return ((-1) ** i) / (2 * i + 1)


# Функция для вычисления следующего значения произведения по формуле Валлиса
def next_wallis_product(i):
    return 4 * (i + 1) ** 2 / (4 * (i + 1) ** 2 - 1)


# Обновленная функция для вычисления числа π
def calculate_pi(n):
    pi_madhava_leibniz = 0
    pi_wallis = 1

    print(f"{'Итерация':<12}{'Мадхава-Лейбниц':<22}{'Валлис':<22}")

    for i in range(n):
        pi_madhava_leibniz += next_madhava_leibniz_term(i)
        pi_wallis *= next_wallis_product(i)

        print(f"{i + 1:<12}{4 * pi_madhava_leibniz:<22.10f}{2 * pi_wallis:<22.10f}")


calculate_pi(10)


# Функция для вычисления числа π по формулам Мадхавы-Лейбница и Валлиса с использованием Polars
def calculate_pi_polars(n):
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

def find_pythagorean_triples(n):
    return [
        (x, y, z)
        for x in range(1, n - 1)
        for y in range(x + 1, n)
        for z in range(y + 1, n + 1)
        if x ** 2 + y ** 2 == z ** 2
    ]


print(f'Пифагоровы тройки: {find_pythagorean_triples(30)}')


# Задание 3
def format_verse(n):
    next_n = n - 1  # Следующее количество бутылок
    # Первая часть строки, которая изменяется в зависимости от количества бутылок
    bottles = lambda x: f"{x} green bottle{'s' if x > 1 else ''} hanging on the wall"
    # Формирование строки куплета
    verse = f"{bottles(n)},\n" * 2 + \
            "And if one green bottle should accidentally fall,\n" + \
            f"There’ll be {bottles(next_n)}.\n"
    return verse if n > 1 else verse.replace("And if", "If that")  # Заменяем начало последней строки для 1 бутылки


# Генерируем и выводим весь текст песни, используя функциональный подход
song_text = "\n".join(map(format_verse, range(10, 0, -1)))
print(song_text)


# Задание 4
def fill_top(matrix, top, left, right, value):
    for i in range(left, right + 1):
        matrix[top][i] = value
        value += 1
    return value


def fill_right(matrix, right, top, bottom, value):
    for i in range(top, bottom + 1):
        matrix[i][right] = value
        value += 1
    return value


def fill_bottom(matrix, bottom, left, right, value):
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = value
        value += 1
    return value


def fill_left(matrix, left, top, bottom, value):
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = value
        value += 1
    return value


def fill_matrix_spirally(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    value, left, right, top, bottom = 1, 0, n - 1, 0, n - 1

    while value <= n * n:
        value = fill_top(matrix, top, left, right, value)
        top += 1
        value = fill_right(matrix, right, top, bottom, value)
        right -= 1
        value = fill_bottom(matrix, bottom, left, right, value)
        bottom -= 1
        value = fill_left(matrix, left, top, bottom, value)
        left += 1

    return matrix


matrix_size = 5
spiral_matrix = fill_matrix_spirally(matrix_size)
for row in spiral_matrix:
    print(row)


# Задание 5
def create_and_fill_matrix(n):
    # Создаем и заполняем матрицу значениями
    matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]
    return matrix


def swap_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        # Обмен значениями главной и побочной диагоналей
        matrix[i][i], matrix[i][n - 1 - i] = matrix[i][n - 1 - i], matrix[i][i]
    return matrix


# Создаем и заполняем матрицу порядка 5
n = 5
matrix = create_and_fill_matrix(n)

print("\nИсходная матрица:")
for row in matrix:
    print(row)

# Обмен значениями главной и побочной диагоналей
swapped_matrix = swap_diagonals(matrix)

print("\nМатрица после обмена диагоналей:")
for row in swapped_matrix:
    print(row)
