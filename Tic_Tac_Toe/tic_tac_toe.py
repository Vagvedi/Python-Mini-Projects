import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # Game variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_active = True
        self.scores = {"X": 0, "O": 0, "Draws": 0}
        
        # Colors
        self.bg_color = "#2c3e50"
        self.button_color = "#34495e"
        self.x_color = "#e74c3c"
        self.o_color = "#3498db"
        self.hover_color = "#4a5f7a"
        
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_font = font.Font(family="Arial", size=24, weight="bold")
        title_label = tk.Label(
            self.root, 
            text="TIC TAC TOE", 
            font=title_font,
            bg=self.bg_color,
            fg="white"
        )
        title_label.pack(pady=20)
        
        # Current player indicator
        self.player_font = font.Font(family="Arial", size=14)
        self.player_label = tk.Label(
            self.root,
            text=f"Player {self.current_player}'s Turn",
            font=self.player_font,
            bg=self.bg_color,
            fg=self.x_color if self.current_player == "X" else self.o_color
        )
        self.player_label.pack(pady=10)
        
        # Score frame
        score_frame = tk.Frame(self.root, bg=self.bg_color)
        score_frame.pack(pady=10)
        
        score_font = font.Font(family="Arial", size=12)
        
        tk.Label(
            score_frame,
            text="Score:",
            font=score_font,
            bg=self.bg_color,
            fg="white"
        ).grid(row=0, column=0, padx=5)
        
        tk.Label(
            score_frame,
            text=f"X: {self.scores['X']}",
            font=score_font,
            bg=self.bg_color,
            fg=self.x_color
        ).grid(row=0, column=1, padx=5)
        
        tk.Label(
            score_frame,
            text=f"O: {self.scores['O']}",
            font=score_font,
            bg=self.bg_color,
            fg=self.o_color
        ).grid(row=0, column=2, padx=5)
        
        tk.Label(
            score_frame,
            text=f"Draws: {self.scores['Draws']}",
            font=score_font,
            bg=self.bg_color,
            fg="white"
        ).grid(row=0, column=3, padx=5)
        
        # Game board frame
        board_frame = tk.Frame(self.root, bg=self.bg_color)
        board_frame.pack(pady=20)
        
        # Create buttons for the game board
        self.buttons = []
        button_font = font.Font(family="Arial", size=20, weight="bold")
        
        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(
                    board_frame,
                    text="",
                    font=button_font,
                    width=5,
                    height=2,
                    bg=self.button_color,
                    fg="white",
                    activebackground=self.hover_color,
                    relief=tk.RAISED,
                    bd=3,
                    command=lambda row=i, col=j: self.make_move(row, col)
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)
        
        # Control buttons frame
        control_frame = tk.Frame(self.root, bg=self.bg_color)
        control_frame.pack(pady=20)
        
        button_font_small = font.Font(family="Arial", size=12)
        
        # New game button
        self.new_game_button = tk.Button(
            control_frame,
            text="New Game",
            font=button_font_small,
            width=12,
            height=2,
            bg="#27ae60",
            fg="white",
            activebackground="#2ecc71",
            relief=tk.RAISED,
            bd=2,
            command=self.reset_game
        )
        self.new_game_button.grid(row=0, column=0, padx=10)
        
        # Reset scores button
        self.reset_scores_button = tk.Button(
            control_frame,
            text="Reset Scores",
            font=button_font_small,
            width=12,
            height=2,
            bg="#e67e22",
            fg="white",
            activebackground="#f39c12",
            relief=tk.RAISED,
            bd=2,
            command=self.reset_scores
        )
        self.reset_scores_button.grid(row=0, column=1, padx=10)
        
    def make_move(self, row, col):
        if self.board[row][col] == "" and self.game_active:
            # Update board
            self.board[row][col] = self.current_player
            
            # Update button
            self.buttons[row][col].config(
                text=self.current_player,
                fg=self.x_color if self.current_player == "X" else self.o_color,
                state=tk.DISABLED,
                disabledforeground=self.x_color if self.current_player == "X" else self.o_color
            )
            
            # Check for winner
            if self.check_winner():
                self.game_active = False
                self.scores[self.current_player] += 1
                self.update_score_display()
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.highlight_winning_line()
            elif self.check_draw():
                self.game_active = False
                self.scores["Draws"] += 1
                self.update_score_display()
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                # Switch player
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_player_label()
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != "":
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        
        return False
    
    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    
    def highlight_winning_line(self):
        # Highlight the winning combination
        # Check rows
        for i, row in enumerate(self.board):
            if row[0] == row[1] == row[2] != "":
                for j in range(3):
                    self.buttons[i][j].config(bg="#27ae60")
                return
        
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != "":
                for i in range(3):
                    self.buttons[i][j].config(bg="#27ae60")
                return
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            for i in range(3):
                self.buttons[i][i].config(bg="#27ae60")
            return
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            self.buttons[0][2].config(bg="#27ae60")
            self.buttons[1][1].config(bg="#27ae60")
            self.buttons[2][0].config(bg="#27ae60")
    
    def update_player_label(self):
        self.player_label.config(
            text=f"Player {self.current_player}'s Turn",
            fg=self.x_color if self.current_player == "X" else self.o_color
        )
    
    def update_score_display(self):
        # Update the score labels
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) and widget != self.root.winfo_children()[1]:
                for child in widget.winfo_children():
                    if isinstance(child, tk.Label) and "X:" in child.cget("text"):
                        child.config(text=f"X: {self.scores['X']}")
                    elif isinstance(child, tk.Label) and "O:" in child.cget("text"):
                        child.config(text=f"O: {self.scores['O']}")
                    elif isinstance(child, tk.Label) and "Draws:" in child.cget("text"):
                        child.config(text=f"Draws: {self.scores['Draws']}")
    
    def reset_game(self):
        # Reset game state
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_active = True
        
        # Reset buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(
                    text="",
                    state=tk.NORMAL,
                    bg=self.button_color,
                    fg="white"
                )
        
        # Update player label
        self.update_player_label()
    
    def reset_scores(self):
        # Reset scores
        self.scores = {"X": 0, "O": 0, "Draws": 0}
        self.update_score_display()
        self.reset_game()

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()
