


import os
import time
import sqlite3
from tkinter import *
import tkinter as tk

import drill_mix_main
import drill_mix_funct







def load_gui(self):

    self.txt_files = StringVar()
    self.dir_path1 = StringVar()
    self.dir_path2 = StringVar()
   
    # Column  0 Buttons
    self.btn1_src = tk.Button(self.master,width=14,height=2, text='Browse',command=lambda:drill_mix_funct.get_src(self))
    self.btn1_src.grid(row=0,column=0,padx=(25,0),pady=(55,10), sticky=W)

    self.btn2_dst = tk.Button(self.master,width=14,height=2, text='Browse',command=lambda:drill_mix_funct.get_dest(self))
    self.btn2_dst.grid(row=1,column=0,padx=(25,0),pady=(5,10), sticky=W)

    self.btn3_move = tk.Button(self.master,width=14,height=3, text='Check files',command=lambda:drill_mix_funct.data_entry(self))
    self.btn3_move.grid(row=2,column=0,padx=(25,0),pady=(5,10), sticky=W)

    # Column 1+ Text Entries
    self.txt_btn1 = tk.Entry(self.master,width=40,text='',textvariable=self.dir_path1)
    self.txt_btn1.grid(row=0, column=1,columnspan=2,padx=(25,0),pady=(55,10),sticky=N+E+W)

    self.txt_b2 = tk.Entry(self.master, width=40,text='',textvariable=self.dir_path2)
    self.txt_b2.grid(row=1, column=1,columnspan=2,padx=(25,0),pady=(5,10),sticky=N+E+W)

  


if __name__ == "__main__":
    pass
