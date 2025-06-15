import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", font=("Arial", 30), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)
        
        self.reset_button = tk.Button(root, text="Reset", font=("Arial", 15), command=self.reset_game)
        self.reset_button.grid(row=3, column=0, columnspan=3)

    def make_move(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            if self.check_winner():
                self.show_winner()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return row[0]
        
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return self.board[0][col]
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        
        return None

    def show_winner(self):
        winner = self.check_winner()
        if winner:
            self.label = tk.Label(self.root, text=f"{winner} wins!", font=("Arial", 20))
            self.label.grid(row=4, column=0, columnspan=3)

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        
        if hasattr(self, "label"):
            self.label.destroy()

root = tk.Tk()
app = TicTacToe(root)
root.mainloop()
