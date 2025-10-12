import tkinter as tk

class  Szukaj:
    def __init__(self, root,x):
        self.root = root
        self.x = x
        self.root.title(" Przeszukiwanie binarne ")
        self.root.geometry("600x150+500+60")

        self.Napis1=tk.Label(root, text="Tablica (wartości oddziel przecinkami): ")
        self.Napis1.grid(column=0, row=2, padx=5, pady=5)

        self.EntryTablica = tk.Entry(root, width=50)
        self.EntryTablica.grid(column=1,row=2)

        self.LabelWynik=tk.Label(root,text=f"Wynik wyszukiwania elementu {x}: ")
        self.LabelWynik.grid(column=0,row=6,padx=5, pady=5)

        self.EntryWynik = tk.Entry(root, width=50)
        self.EntryWynik.grid(column=1,row=6)

        self.przyciskPobierz = tk.Button (root, text=" Pobierz tablicę ", command= self.pobierz)
        self.przyciskPobierz.grid(column=0, row=8)

        self.przyciskZnajdz = tk.Button (root, text=f" Znajdź {self.x} ", command= self.czyJest)
        self.przyciskZnajdz.grid(column=1, row=8)

        self.przyciskCzysc = tk.Button (root, text=" Czyść ", command= self.czysc)
        self.przyciskCzysc.grid(column=2, row=8)


        self.tab=[]
                
    def czysc(self):
        self.EntryTablica.delete(0, tk.END)
        self.EntryWynik.delete(0, tk.END)


    def pobierz(self):
        data=self.EntryTablica.get()
        data = data.split(",")
        self.tab=[int(x) for x in data]
        print(self.tab)
        self.left = 0
        self.right = len(self.tab) -1

    
                    
    def szukaj_rec(self, left,right):
        if left>right:
            return -1
        else:
            mid=(left+right)//2
            if self.tab[mid]==self.x:
                return mid
            else:
                if self.x<self.tab[mid]:
                    return self.szukaj_rec(left,mid-1)
                else:
                    return self.szukaj_rec(mid+1, right)

    def czyJest(self):
        if self.szukaj_rec(self.left, self.right)==-1:
            self.EntryWynik.insert(tk.END,f"Tablica nie zawiera elementu {self.x} ")
        else:
            self.EntryWynik.insert(tk.END,f"Element {self.x} został znaleziony ")
        
                

def main(args):
    root =tk.Tk()
    app = Szukaj(root,5)
    root.mainloop()


if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))        

        
    
