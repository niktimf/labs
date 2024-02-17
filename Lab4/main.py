import tkinter as tk
from tkinter import messagebox


# Определяем класс TicTacToe для игры "Крестики-нолики"
class TicTacToe:
    """
    Класс TicTacToe для игры "Крестики-нолики"
    """
    def __init__(self):
        """
        Конструктор класса TicTacToe. Инициализирует основные переменные и игровое поле.
        """
        self.root = tk.Tk()  # Создаем главное окно
        self.root.title("Крестики-нолики")  # Заголовок окна
        self.player = 1  # Игрок 1 играет "X", игрок -1 играет "O"
        self.game_over = False  # Переменная для отслеживания окончания игры
        self.board = [[0] * 3 for _ in range(3)]  # Инициализируем игровое поле
        self.buttons = [[None for _ in range(3)] for _ in range(3)]  # Кнопки для игрового поля
        self.initialize_board()  # Вызов функции для инициализации игрового поля
        # Создаем кнопку для перезапуска игры
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3)  # Располагаем кнопку на экране

    def run(self):
        """
        Запускает главный цикл обработки событий Tkinter.
        """
        self.root.mainloop()

    def initialize_board(self):
        """
        Инициализирует игровое поле, создавая кнопки и располагая их в окне.
        """
        for i in range(3):
            for j in range(3):
                # Создаем кнопку и устанавливаем ее параметры
                b = tk.Button(self.root, font=("Arial", 24), width=5, height=2,
                              command=lambda i=i, j=j: self.on_click(i, j))
                b.grid(row=i, column=j)  # Располагаем кнопку на экране
                self.buttons[i][j] = b  # Сохраняем кнопку в массиве

    def on_click(self, row, col):
        """
        Обрабатывает нажатие на кнопку игрового поля.
        :param row: номер строки кнопки
        :param col: номер столбца кнопки
        """
        if self.board[row][col] == 0 and not self.game_over:
            self.board[row][col] = self.player  # Обновляем состояние игрового поля
            self.buttons[row][col].config(text=('X' if self.player == 1 else 'O'))  # Обновляем текст кнопки
            if self.check_win(self.player):  # Проверяем, есть ли победитель
                messagebox.showinfo("Победа", f"Игрок {'X' if self.player == 1 else 'O'} победил!")
                self.game_over = True
            elif self.check_draw():  # Проверяем, есть ли ничья
                messagebox.showinfo("Ничья", "Игра закончилась вничью!")
                self.game_over = True
            self.player *= -1  # Смена игрока

    def check_win(self, player):
        """
        Проверяет, выиграл ли текущий игрок.
        :param player: текущий игрок (1 или -1)
        :return: True, если игрок выиграл, иначе False
        """
        for i in range(3):
            # Проверяем строки и столбцы
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        # Проверяем диагонали
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == player or
                self.board[0][2] == self.board[1][1] == self.board[2][0] == player):
            return True
        return False

    def check_draw(self):
        """
        Проверяет, закончилась ли игра вничью.
        :return: True, если игра вничью, иначе False
        """
        return all(self.board[row][col] != 0 for row in range(3) for col in range(3))

    def restart_game(self):
        """
        Перезапускает игру, сбрасывая состояние игрового поля и переменные.
        """
        self.player = 1  # Сброс игрока
        self.game_over = False  # Сброс состояния игры
        self.board = [[0] * 3 for _ in range(3)]  # Сброс игрового поля
        for row in self.buttons:
            for button in row:
                button.config(text='')  # Очистка текста кнопок


# Создаем экземпляр игры и запускаем ее
game = TicTacToe()
game.run()
