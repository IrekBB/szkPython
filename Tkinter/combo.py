import tkinter as tk
from tkinter import ttk
import sys

class App(tk.Tk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("ComboBox")
        self.geometry("200x100")
        self.resizable(width=True, height=False)
        self.my_string_var= tk.StringVar()
        self.my_result_var = tk.StringVar()
        combobox = ttk.Combobox(self, textvariable=self.my_string_var,
                                values = ["Option 1", "Option 2", "Option 3"])
        
        button = ttk.Button(self,text="OK",command=self.foo)
        label = ttk.Label(self,textvariable=self.my_result_var)
        combobox.pack()
        button.pack()
        label.pack()
    
    def foo(self):
        if self.my_string_var.get():
            self.my_result_var.set(self.my_string_var.get())



if __name__=="__main__":
    app = App()
    app.mainloop()