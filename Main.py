import tkinter as tk
from GambitGUI import GambitGUI
from GambitBoard import GambitGame

root = tk.Tk()
game = GambitGame()
game_gui = GambitGUI(root, game)
root.mainloop()