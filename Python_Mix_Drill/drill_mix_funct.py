

import os
import time
import sqlite3
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import shutil

import drill_mix_main
import drill_mix_gui






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




def get_src(self):
    dirname1 = filedialog.askdirectory()
    self.dir_path1.set(dirname1)

def get_dest(self):
    dirname2 = filedialog.askdirectory()
    self.dir_path2.set(dirname2)



def create_db(self):
    conn = sqlite3.connect('py_123')
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName TEXT, \
            col_modified TEXT)")
        
        conn.commit()
    conn.close()

    
def data_entry(self):
    conn = sqlite3.connect('py_123')
    with conn:
        c = conn.cursor()
        path = self.dir_path1.get()
        myDir = os.listdir(path)
        for file in myDir:
            if file.endswith(".txt"):
                theFile = os.path.join(path, file)
                ModTime = os.path.getmtime(theFile)
                realTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(ModTime))               
                c.execute("INSERT INTO tbl_files(col_fileName, col_modified) VALUES(?,?)",(file,realTime))
                shutil.move(theFile,self.dir_path2.get())
                print(file, realTime,"File copied successfully.")
        conn.commit()
    conn.close()




        

        


if __name__ == "__main__":
    pass
