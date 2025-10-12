import tkinter as tk
from tkinter.messagebox import showinfo

class MyApp ():
    def __init__(self, root):
        self.root = root
        self.root.title(" WZOREK ")
        self.root.geometry("550x400+500+60")
        self.plotno = tk.Canvas(bg="white", width=300, height = 300)
        self.plotno.grid(column=2, row=2, padx=1, pady=1)
        self.napisLg = tk.Label(root, text=" lg =", padx=10)
        self.napisLg.grid(column=0, row=1)
        self.editLg = tk.Entry(root, width=6)
        self.editLg.insert(tk.END,'20')
        self.editLg.grid(column=1, row=1)
        self.napisXY=tk.Label(root, text=" x, y =")
        self.napisXY.grid(column=2,row=1)
        self.editXY = tk.Entry(root, width=8)
        self.editXY.insert(tk.END,'5, 5 ')
        self.editXY.grid(column=3, row=1)
        self.przyciskRysuj = tk.Button (root, text=" Rysuj ", command= self.clickedRysuj)
        self.przyciskRysuj.grid(column=0, row=3)
        self.przyciskCzysc = tk.Button (root, text=" Czyść ", command= self.clickedCzysc)
        self.przyciskCzysc.grid(column=1, row=3)
        self.n = 4

    def clickedCzysc(self):
        self.editXY.delete(0, tk.END)
        self.editLg.delete(0, tk.END)
        self.plotno.delete("all")
        self.plotno.grid(column=2, row=2, padx=1, pady=1)
 
    def clickedRysuj(self):
        lg = self.getLg()
        x,y= int(self.getXY()[0]),int(self.getXY()[1])
        self.rysuj_wzorek(self.n, lg, x, y)
        
        
    
    def getXY(self):
        if self.editXY.get()!="":
            return self.editXY.get().split(",")
        else:
            showinfo("Window", "Uwaga! Podaj współrzedne lewego wierzchołka kwadratu. ")
            return [0,0]

    def getLg(self):
        if self.editLg.get()!="":
            return int(self.editLg.get())
        else:
            showinfo("Window", "Uwaga! Uzupełnij długość boku kwadratu.")
            return 0

    def rysuj_wzorek(self, n, lg, x, y):
        if n>0:
            #Kwadrat
            self.plotno.create_line(x,y, x+lg,y)
            self.plotno.create_line(x+lg, y, x+lg, y+lg)
            self.plotno.create_line(x+lg,y+lg,x, y+lg)
            self.plotno.create_line(x, y+lg, x,y)
            #Cztery koła wewnętrzne
            self.plotno.create_oval(x, y, x+lg/2, y+lg/2)
            self.plotno.create_oval(x+lg/2, y, x + lg/2, y+lg/2)
            self.plotno.create_oval(x, y+lg/2, x+ lg/2, y + lg)
            self.plotno.create_oval(x+lg/2, y+lg/2, x+lg, y+lg)
            # Wzorki w kołach wewnetrznych powielają schemat główny, ale w mniejszm rozmiarze
            self.rysuj_wzorek (n-1, lg/2, x, y)
            self.rysuj_wzorek (n-1, lg/2, x+lg/2, y)
            self.rysuj_wzorek (n-1, lg/2, x, y+lg/2)
            self.rysuj_wzorek (n-1, lg/2, x+lg/2, y+lg/2)
            
        
        
        
        

        
        
        

def main(args):
    root =tk.Tk()
    app = MyApp(root)
    root.mainloop()
    
if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))
