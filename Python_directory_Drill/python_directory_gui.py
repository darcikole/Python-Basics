

from tkinter import *
import tkinter as tk

import python_directory_main
import python_directory_funct



    
def load_gui(self):
        
    
    dir_path = StringVar(self)

    # Column 0 Button
    self.button_browse1 = tk.Button(self.master,width=14,height=2, text='Browse...',command=lambda:python_directory_funct.get_directory(self))
    self.button_browse1.grid(row=0,column=0,padx=(25,0),pady=(55,10), sticky=W)

    # Column 1 Entry
    self.txt_b1 = tk.Entry(self.master,width=40,textvariable = dir_path)
    self.txt_b1.grid(row=0, column=1,columnspan=2,padx=(25,0),pady=(55,10),sticky=E+W)

    
    s=dir_path.get()



if __name__ == "__main__":
    pass
