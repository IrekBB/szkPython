import tkinter as tk

class MyApp ():
    def __init__(self, root):
        self.root = root
        self.root.title(" Spirala w Pytonie ")
        self.root.geometry("550x400+500+60")

        self.paramAlpha = 20
        self.paramLg = 180

        self.napisAlpha = tk.Label(root, text=" alpha =")
        self.napisAlpha.grid(column=0, row=1, padx=5, pady=5)

        self.napis2 = tk.Label(root, text=" lg =")
        self.napis2.grid(column=0, row=2)

        self.przyciskCzysc = tk.Button(root, text=" Czyść ", command = self.clickedCzysc)
        self.przyciskCzysc.grid(column=1, row=0, padx=5, pady=5)

        self.przyciskRysuj = tk.Button (root, text=" Rysuj ", command= self.clickedRysuj)
        self.przyciskRysuj.grid(column=0, row=0)

        self.editAlpha = tk.Entry(root, width=6)
        self.editAlpha.insert(tk.END,'70')
        self.editAlpha.grid(column=1, row=1)

        self.editLg = tk.Entry(root, width=5)
        self.editLg.insert(tk.END, '180')
        self.editLg.grid(column=1, row=2, padx=5, pady=5)

        self.plotno = tk.Canvas(bg="white", width=300, height = 300)

        self.x = 5
        self.y = 5
        

    def clickedCzysc(self):
        self.editAlpha.delete(0, tk.END)
        self.editLg.delete(0, tk.END)
        self.plotno.delete("all")

    def clickedRysuj(self):
        self.plotno.delete("all")                # Czyścimy pole rysowania
        self.paramAlpha=int(self.editAlpha.get())     # Odczyt wartości Alpha
        self.paramLg=int(self.editLg.get())           # Odczyt wartości Lg
        print(self.paramLg, self.paramAlpha)
        self.rysuj_spirala(self.paramAlpha, self.paramLg,self.x,self.y)

    def rysuj_spirala(self,paramAlpha, paramLg, x, y):
        if (paramLg > 0 and paramLg > paramAlpha):
            self.plotno.create_line(x, y, x + paramLg, y)
            self.plotno.create_line(x + paramLg, y, x + paramLg, y + paramLg)
            self.plotno.create_line(x + paramLg, y + paramLg, x + paramAlpha, y + paramLg, dash=(3, 3))
            self.plotno.create_line(x + paramAlpha, y + paramLg, x + paramAlpha, y + paramAlpha)
            self.rysuj_spirala(paramAlpha, paramLg - 2 * paramAlpha, x + paramAlpha, y + paramAlpha)
        self.plotno.grid(column=2, row=2, padx=1, pady=1)

    

def main(args):
    root =tk.Tk()
    app = MyApp(root)
    root.mainloop()
    
if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))

