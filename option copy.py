# Su Jin Ahn 75216135
# Project 5_GUI, Option Window + GUI

import tkinter
import othello_logic

DEFAULT = ('Helvetica', 14)


class NameDialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()
        
        #info label
        info_label = tkinter.Label(
            master = self._dialog_window, text = 'Welcome to Othello Game',
            font = DEFAULT)

        info_label.grid(
            row = 0, column = 0, columnspan = 2, padx = 150, pady = 10,
            sticky = tkinter.W)

        #row label
        row_label = tkinter.Label(
            master = self._dialog_window, text = 'Number of Rows: ',
            font = DEFAULT)

        row_label.grid(
            row = 1, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._row_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT)

        self._row_entry.grid(
            row = 1, column = 1, padx = 10, pady = 1,
            sticky = tkinter.W + tkinter.E)

        
        #col label
        col_label = tkinter.Label(
            master = self._dialog_window, text = 'Number of Columns: ',
            font = DEFAULT)

        col_label.grid(
            row = 2, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        self._col_entry = tkinter.Entry(
            master = self._dialog_window, width = 20, font = DEFAULT)

        self._col_entry.grid(
            row = 2, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)


        #first move selection
        first_move = tkinter.Label(
            master = self._dialog_window, text = 'Who wants to move first? ',
            font = DEFAULT)

        first_move.grid(row=3, column=0, padx = 10, pady = 10, sticky = tkinter.W)

        optionList = ('B', 'W')
        self._first_move = tkinter.StringVar()
        self._first_move.set(optionList[0])
        self._first_move_om = tkinter.OptionMenu(self._dialog_window, self._first_move, *optionList)
        self._first_move_om.grid( row = 3, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)
           


        #center move selection        
        center_label = tkinter.Label(
            master = self._dialog_window, text = 'Which disc to be top-left/right bottom?: ',
            font = DEFAULT)

        center_label.grid(
            row = 4, column = 0, padx = 10, pady = 10, sticky = tkinter.W)

        optionList = ('B', 'W')
        self._center = tkinter.StringVar()
        self._center.set(optionList[0])
        self._center_entry = tkinter.OptionMenu(self._dialog_window, self._center, *optionList)
        self._center_entry.grid (row=4, column = 1, padx = 10, pady = 1, sticky = tkinter.W + tkinter.E)

        

        #ok & cancel
        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 5, column = 0, columnspan = 2, padx = 10, pady = 10, sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            master = button_frame, text = 'Start', font = DEFAULT,
            command = self._on_ok_button)

        ok_button.grid(row = 5, column = 0, padx = 10, pady = 10)

        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 5, column = 1, padx = 10, pady = 10)

        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.columnconfigure (1, weight = 1)

        self._ok_clicked = False
        self._row_number = 0
        self._col_number = 0



    def show(self) -> None:
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self) -> bool:
        return self._ok_clicked

    def get_row_number(self) -> str:
        return self._row_number

    def get_col_number(self) -> str:
        return self._col_number

    def get_first_move(self) -> str:
        return self._first_move

    def get_center_disc(self) -> str:
        return self._center

    def _on_ok_button(self) -> None:
        self._ok_clicked = True
        self._row_number = self._row_entry.get()
        self._col_number = self._col_entry.get()
        self._first_move = self._first_move.get()
        self._center = self._center.get()

        

        self._dialog_window.destroy()
        return self._row_number, self._col_number, self._first_move, self._center


    def _on_cancel_button(self) -> None:
        self._dialog_window.destroy()



class board():
    def __init__(self):
        
        self._root_window = tkinter.Tk()
        
        self.user_input = NameDialog()

        self._root_window.wait_window(self.user_input._dialog_window)

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 600, height = 600,
            background = '#2FA611')



    def start(self):
      

        self._root_window.rowconfigure(0, weight = 10)
        self._root_window.columnconfigure(0, weight = 10)

        self._canvas.grid(row = 0, column = 0,
                          sticky = tkinter.E + tkinter.W + tkinter.S + tkinter.N)
        
     

        self._root_window.bind("<Configure>", self.on_resize)
        self._root_window.mainloop()
        
   


    def on_resize(self,event):
        row = int(self.user_input.get_row_number())
        col = int(self.user_input.get_col_number())
        self._canvas.delete(tkinter.ALL)

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        for x in range(row):
            self._canvas.create_line(0, (x/row)*height, width, (x/row)*height, fill = 'black')
            y = (x/row)/height

        for y in range(col):
            self._canvas.create_line((y/col)*width, 0, (y/col)*width, height, fill = 'black')
            print('ycol', (y/col)*width)
            
        
        
            
        self._canvas.create_oval((row/2)-1,(col/2)-1,row/2,col/2, fill = 'white')
      
        

    

if __name__ == '__main__':
    x = board()
    x.start()
  
 


   
   
        
                               
