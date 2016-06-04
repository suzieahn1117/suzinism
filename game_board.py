# Su Jin Ahn 75216135
# Project 5 GUI, Game Board

import othello_logic
import tkinter
import option

class board():
    def __init__(self, row, col, move, center):
        self.row = int(row)
        self.col = int(col)
        self.first_move = move
        self.center = center
  
        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = '#2FA611')
        

        self._canvas.grid(row = 0, column = 0,
                          sticky = tkinter.E + tkinter.W + tkinter.S + tkinter.N)

        self._root_window.rowconfigure(0, weight = 10)
        self._root_window.columnconfigure(0, weight = 10)

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        print(self.row)

    def run(self) -> None:
      
        self._root_window.mainloop()








