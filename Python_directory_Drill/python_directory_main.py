

from tkinter import *
import tkinter as tk

import python_directory_funct
import python_directory_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # master frame config
        self.master = master
        self.master.minsize(600,150) # (w,h)
        self.master.maxsize(600,150)

        self.master.title("Choose File")
        self.master.configure(bg="#f0f0f0")

        # center window
        python_directory_funct.center_window(self,600,150)

        # import gui
        python_directory_gui.load_gui(self)

        
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

