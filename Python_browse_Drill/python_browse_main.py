

from tkinter import*
import tkinter as tk

import python_browse_funct
import python_browse_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #master frame configuration
        self.master = master
        self.master.minsize(600,250)
        self.master.maxsize(600,250)
        self.master.title("Check files")
        self.master.configure(bg="#f0f0f0", highlightbackground="orange", highlightcolor="orange", highlightthickness="1")

        #center window function
        python_browse_funct.center_window(self,600,300)

        #load GUI
        python_browse_gui.load_gui(self)
 

        
    
   

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
