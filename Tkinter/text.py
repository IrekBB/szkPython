import tkinter as tk
from tkinter import ttk
import sys

class App(tk.Tk):
     def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Text Widget")
        self.geometry("300x300")
        self.resizable(width=False, height=False)
        mytext = tk.Text(self)
        mytext.insert('1.0','I love my text widget!')
        mytext.insert('1.2','REALLY ')
        # get the whole string
        mytext.get('1.0', tk.END)
        # delete the last character.
        # Note that there is always a newline character
        # at the end of the input, so we backup 2 chars.
        mytext.delete('end - 2 chars')
        mytext.pack()


def main(args):
    app = App()
    app.mainloop()

if __name__=="__main__":
    sys.exit(main(sys.argv))