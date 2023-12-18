import tkinter as tk
from GambitBoard import GambitGame
from BeepBoopBot import GambitBot

class GambitGUI:
    def __init__(self, master, gamen, bot):
        self.master = master
        self.game = game
        self.selected_piece = None
        self.bot = bot

        master.title('Gambit Game')
        self.canvas = tk.Canvas(master, width=250, height=350)  # Smaller canvas
        self.canvas.pack()

        self.draw_board()
        self.draw_pawns()
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def draw_board(self):
        for i in range(7):
            for j in range(5):
                color = 'white' if (i + j) % 2 == 0 else 'gray'
                self.canvas.create_rectangle(j*50, i*50, j*50+50, i*50+50, fill=color)  # Smaller squares

    def draw_pawns(self):
        self.canvas.delete("pawn")  # Remove old pawns
        for i in range(7):
            for j in range(5):
                pawn = self.game.board[i][j]
                if pawn == 'P1':
                    self.canvas.create_oval(j*50+12, i*50+12, j*50+38, i*50+38, fill='black', tags="pawn")
                elif pawn == 'P2':
                    self.canvas.create_oval(j*50+12, i*50+12, j*50+38, i*50+38, fill='red', tags="pawn")

    def on_canvas_click(self, event):
        if self.game.current_turn == 'P1' and not self.game.winner:  # Player's turn
            col = event.x // 50  # Adjusted for smaller squares
            row = event.y // 50
            if self.selected_piece:
                from_row, from_col = self.selected_piece
                if self.game.move_pawn(from_row, from_col, row, col):
                    self.draw_pawns()
                    self.check_game_over()
                    self.bot_move()  # Invoke bot's move
                self.selected_piece = None
            else:
                if self.game.board[row][col] == 'P1':  # Select only if there's a player's pawn
                    self.selected_piece = (row, col)

    def bot_move(self):
        if self.game.current_turn == 'P2' and not self.game.winner:
            bot_move = self.bot.minimax(self.game, 3, 'P2')  # This should return a move tuple
            if bot_move:
                # Ensure bot_move is a tuple with 4 elements
                if isinstance(bot_move, tuple) and len(bot_move) == 4:
                    self.game.move_pawn(*bot_move)
                    self.draw_pawns()
                    self.check_game_over()
                else:
                    # Handle the case where bot_move is not in the expected format
                    print("Invalid move format from bot")

    def check_game_over(self):
        if self.game.winner:
            self.show_winner()  # Implement this method to display the winner
            self.master.destroy()
root = tk.Tk()
game = GambitGame()
bot = GambitBot(game)  # Assuming GambitBot is properly implemented
gui = GambitGUI(root, game, bot)
root.mainloop()