import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Крестики-нолики")
        self.player = 1  # Игрок 1 играет "X", -1 играет "O"
        self.game_over = False
        self.board = [[0] * 3 for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.initialize_board()
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3)

    def run(self):
        self.root.mainloop()

    def initialize_board(self):
        for i in range(3):
            for j in range(3):
                b = tk.Button(self.root, font=("Arial", 24), width=5, height=2, command=lambda i=i, j=j: self.on_click(i, j))
                b.grid(row=i, column=j)
                self.buttons[i][j] = b

    def on_click(self, row, col):
        if self.board[row][col] == 0 and not self.game_over:
            self.board[row][col] = self.player
            self.buttons[row][col].config(text=('X' if self.player == 1 else 'O'))
            if self.check_win(self.player):
                messagebox.showinfo("Победа", f"Игрок {'X' if self.player == 1 else 'O'} победил!")
                self.game_over = True
            elif self.check_draw():
                messagebox.showinfo("Ничья", "Игра закончилась вничью!")
                self.game_over = True
            self.player *= -1

    def check_win(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or all(self.board[j][i] == player for j in range(3)):
                return True
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == player or
                self.board[0][2] == self.board[1][1] == self.board[2][0] == player):
            return True
        return False

    def check_draw(self):
        return all(self.board[row][col] != 0 for row in range(3) for col in range(3))

    def restart_game(self):
        self.player = 1
        self.game_over = False
        self.board = [[0] * 3 for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.config(text='')


game = TicTacToe()
game.run()
