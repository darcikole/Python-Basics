

import os
import time
import sqlite3
from tkinter import *
import tkinter as tk

import drill_mix_funct
import drill_mix_gui






class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # master frame config
        self.master = master
        self.master.minsize(600,270) # (w,h)
        self.master.maxsize(600,270)

        self.master.title("Choose File")
        self.master.configure(bg="#f0f0f0")

        # center window
        drill_mix_funct.center_window(self,600,270)

        # import gui
        drill_mix_gui.load_gui(self)

        # import db
        drill_mix_funct.create_db(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
