import tkinter as tk
from tkinter import ttk

class MyApplication(tk.Tk):
    """Widgets test"""
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.my_text_var = tk.StringVar()
        self.my_result_var = tk.StringVar()
        self.title ("Hello Entry in Tkinter")
        self.geometry("300x70")
        self.resizable(width=False, height=False)
        my_entry = ttk.Entry(self, textvariable=self.my_text_var, show="*")
        my_entry.pack()
        ch_button = ttk.Button(self,text="Change", command=self.on_change)
        ch_button.pack()
        result_label = ttk.Label(self,textvariable=self.my_result_var)
        result_label.pack()
        self.columnconfigure(0,weight=1)

    
    def on_change(self):
        if self.my_text_var.get().strip():
            self.my_result_var.set("Result:" + self.my_text_var.get())
            
            

        
    
def main(args):   
    app = MyApplication()
    app.mainloop()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))