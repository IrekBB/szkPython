import tkinter as tk
from tkinter import ttk
import sys

LOGIN = "Ireneusz"
PASSWD = "123"


class App(tk.Tk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("EntryBox")
        self.geometry("300x200")
        self.resizable(width=False, height=False)
        self.login = tk.StringVar()
        self.passwd = tk.StringVar()
        self.result = tk.StringVar()
        enter_login = ttk.Entry(self,textvariable=self.login)
        enter_passwd = ttk.Entry(self, show="*",textvariable=self.passwd)
        login_label=ttk.Label(self,text="Login: ")
        passwd_label = ttk.Label(self, text="Password: ")
        button = ttk.Button(self, text="Ok", command=self.check)
        result_label = ttk.Label(self,textvariable=self.result)
        login_label.grid(row=0,column=0, sticky = 'E', pady = 4)
        enter_login.grid(row=0,column=1,sticky = 'E', pady = 4)
        passwd_label.grid(row=1,column=0,sticky = 'E', pady = 6)
        enter_passwd.grid(row=1,column=1,sticky = 'E', pady = 6)
        button.grid(row=2,column=0, columnspan=2,pady=20)
        result_label.grid(row=3,column = 0, pady=10, sticky='E')

    def check(self):
        if self.login.get().strip()==LOGIN and self.passwd.get().strip()==PASSWD:
            self.result.set("Witaj w systemie")
        else:
            self.result.set("Błąd Logowania")

  



def main(args):
    app = App()
    app.mainloop()

if __name__=="__main__":
    sys.exit(main(sys.argv))

