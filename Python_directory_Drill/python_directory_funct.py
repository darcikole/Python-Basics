

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os



import python_directory_main
import python_directory_gui


def center_window(self, w, h):
    # Gets the requested values of the height and width.
    sc_width = self.master.winfo_screenwidth()
    sc_height = self.master.winfo_screenheight()

         
    # Gets both half the screen width/height and window width/height
    x = int((sc_width/2) - (w/2))
    y= int((sc_height/2) - (h/2))
         
    # Positions the window in the center of the page.
    centerGeo = self.master.geometry("{}x{}+{}+{}".format(w,h,x, y))
    return centerGeo


def get_directory(self):
    global dirname
    dirname = filedialog.askdirectory()
    dir_path.set(dirname)
        





if __name__ == "__main__":
    pass
