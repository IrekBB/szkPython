import tkinter as tk
import sys

class App(tk.Tk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Spinbox")
        self.geometry("200x50")
        self.resizable(width=True, height=False)
        self.my_double_var = tk.DoubleVar() 
        result_label=tk.Label(self, textvariable=self.my_double_var)
        result_label.pack()
        my_spinbox = tk.Spinbox(self,
                                from_=0.5,
                                to=52.0,
                                increment=.01,
                                textvariable=self.my_double_var,
                                )
        my_spinbox.pack()
def main(args):
    app = App()
    app.mainloop()

if __name__=="__main__":
    sys.exit(main(sys.argv))


