"""Hello World application for Tkinter"""
def main(args):
    root = Tk()
    root.title("Hello Tkinter")
    root.geometry("200x50")
    root.resizable(width=True, height=False)
    label = Label(root, text="Hello World")
    label.pack()
    root.mainloop()

if __name__=="__main__":
    from tkinter import *
    from tkinter.ttk import *
    import sys
    sys.exit(main(sys.argv))

