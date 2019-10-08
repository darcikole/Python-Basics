

from tkinter import*
import tkinter as tk

import python_browse_main
import python_browse_funct


def load_gui(self):
   
    # Column  0 Buttons
    self.button_browse1 = tk.Button(self.master,width=14,height=2, text='Browse...')
    self.button_browse1.grid(row=0,column=0,padx=(25,0),pady=(55,10), sticky=W)

    self.button_browse2 = tk.Button(self.master,width=14,height=2, text='Browse...')
    self.button_browse2.grid(row=1,column=0,padx=(25,0),pady=(5,10), sticky=W)

    self.button_check = tk.Button(self.master,width=14,height=3, text='Check for files...')
    self.button_check.grid(row=2,column=0,padx=(25,0),pady=(5,10), sticky=W)

    # Column 1+ Text Entries
    self.txt_b1 = tk.Entry(self.master,width=40,text='')
    self.txt_b1.grid(row=0, column=1,columnspan=2,padx=(25,0),pady=(55,10),sticky=N+E+W)

    self.txt_b2 = tk.Entry(self.master, width=40,text='')
    self.txt_b2.grid(row=1, column=1,columnspan=2,padx=(25,0),pady=(5,10),sticky=N+E+W)

    # Column 2 Button
    self.button_close = tk.Button(self.master, width=14, height=3, text='Close Program')
    self.button_close.grid(row=2,column=2,padx=(75,0),pady=(5,10), sticky=E)

    


if __name__ == "__main__":
    pass
