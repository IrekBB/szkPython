class GrafTabl:
    def __init__(self, N, opis):
        self.N = N
        self.opis = opis
        self.G = [0] * N     # G -graf zamodeloway przy uzyciu tablicy [N][N]
        self.R = [0] * N     # R - matryca kierowania ruhem zamodelowana przy użyciu
                             # tablicy [N][N]
        for i in range(N):   # Inicjacja drugiego wymiaru tablic [N][N]
            self.G[i] = [0] * N
            self.R[i] = [0] * N
        
        self.V = [0] * N   # Tablica o rozmiarze [N] przechowująca na uzytek algorytmu
                           # przeszukiwania DFS
                           # informację, czy wierzchołek był już badany (wartość: 1)
                           # czy nie (wartość: 0)
    
    def zeruj(self):
        for i  in range(self.N):
            for j in range(self.N):
                self.G[i][j] = 0    # Konwencja: 0=brak krawędzi
    
    def add(self, i, j, val):   # dopisz węzeł
        if i < self.N and j < self.N:
            self.G[i][j] = val
        else:
            print ("Indeks(y) poza zakresem tablicy: " + i + "!")
    
    def get(self, i, j):      # Zwróć wartość węzła
        if i < self.N and j < self.N:
            return self.G[i][j]
        else:
            return None      # Umowny błąd
    
    def wypisz(self):     # Wypisz graf G
        print("Graf: " + self.opis)
        for i in range(self.N):
            for j in range(self.N):
                # 100000 niech oznacza umowny brak krawędzi(nieskończony koszt przejścia)
                if self.G[i][j] != 100000:
                    print(f"{self.G[i][j]:3}", end=" ")
                else:
                    print(" - ", end=" ")
            print()
        print()


