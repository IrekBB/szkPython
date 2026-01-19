import tkinter as tk
from tkinter import ttk
import sys

class App(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("ChecBox Window")
        self.geometry("300x200")
        self.resizable(width=False, height=False)
        self.my_boolean_var_1 = tk.BooleanVar()
        self.my_boolean_var_2 = tk.BooleanVar()
        self.text =  tk.StringVar()

        my_checkbutton_1 = ttk.Checkbutton(
            self,
            text ="Check to make this option True",
            variable = self.my_boolean_var_1,
            onvalue=True, offvalue=False,
            command=self.foo,
        )
        my_checkbutton_2 = ttk.Checkbutton(
            self,
            text ="Check to make this option True",
            variable = self.my_boolean_var_2,
            onvalue=True, offvalue=False,
            command=self.foo,
        )
        result_label=ttk.Label(self,textvariable=self.text) 
        my_checkbutton_1.pack()
        my_checkbutton_2.pack()
        result_label.pack()
    
    def foo(self):
        if self.my_boolean_var_1.get()==True and self.my_boolean_var_2.get()==True :
            self.text.set("Checkbox1 + Checkbox2")
        elif self.my_boolean_var_1.get()==True and self.my_boolean_var_2.get()==False:
            self.text.set("Checkbox1") 
        elif self.my_boolean_var_1.get()==False and self.my_boolean_var_2.get()==True:
            self.text.set("Checkbox2")  
        else:
            self.text.set("") 

       

    

def main(args):
    app = App()
    app.mainloop()

if __name__=="__main__":
    sys.exit(main(sys.argv))

