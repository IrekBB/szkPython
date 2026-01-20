from tkinter import *
from tkinter import ttk

def has_five_or_less_chars(string):
    return len(string) <= 5

root = Tk()
root.title("Walidacja pola tekstowego")
root.geometry("300x100")
root.resizable(width=True,height=False)

wrapped_function = root.register(has_five_or_less_chars)
vcmd = (wrapped_function, '%P')
five_char_input = ttk.Entry(root, validate='key', validatecommand=vcmd)

five_char_input.pack()
root.mainloop()