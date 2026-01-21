import tkinter as tk

root = tk.Tk()
root.title("Tkinter Label Image")

photo = tk.PhotoImage(file=r"E:\Users\opiekun\Documents\Tkinter\otje.png").subsample(2)
label = tk.Label(root, image=photo)
label.pack(expand=True)

root.mainloop()