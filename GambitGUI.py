import tkinter as tk


class GambitGUI:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        self.selected_piece = None

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
        col = event.x // 50  # Adjusted for smaller squares
        row = event.y // 50
        if self.selected_piece:
            from_row, from_col = self.selected_piece
            if self.game.move_pawn(from_row, from_col, row, col):
                self.draw_pawns()
            self.selected_piece = None
        else:
            if self.game.board[row][col] in ['P1', 'P2']:  # Select only if there's a pawn
                self.selected_piece = (row, col)
        if self.game.winner:
            self.master.destroy()