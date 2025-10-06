import numpy as np
MAX_VERTEX = 20
SIZE = 20


class Vertex:
    def __init__(self, lab):
        self.label = lab
        self.wasVisited = False

class StackX:
    def __init__(self):
        self.stos = np.empty(MAX_VERTEX, dtype='int')         # Właściwa kolekcja danych
        self.top = -1
        
    
    def  push(self, j):  # zapisz element na stosie
        self.top = self.top + 1
        self.stos[self.top] = j
    
    def pop(self):
        k = self.stos[self.top]
        self.top = self.top - 1
        return k
    
    def peek(self):
        return self.stos[self.top]
    
    def isEmpty(self):
        return self.top == -1


class Graph:
    def __init__ (self):
        self.vertexList = np.empty([MAX_VERTEX], dtype = Vertex)
        self.adjMat = np.empty([MAX_VERTEX , MAX_VERTEX], dtype='int')
        self.nVerts = 0
        self.theStack = StackX()
    
    def addVertex(self,lab):
        self.vertexList[self.nVerts] = Vertex(lab)
        self.nVerts = self.nVerts + 1

    def addEdge(self, start, end):
        self.adjMat[start][end] = 1
        self.adjMat[end][start] = 1

    def displayVertex(self,v):
        print(self.vertexList[v].label, end="")

    def getAdjUnvisitedVertex(self, v):  # Zwraca nieodwiedzony wierzchołek przyległy do v
        for j in range(self.nVerts):
            if self.adjMat[v][j]==1 and self.vertexList[j].wasVisited == False:
                return j
        return -1
    
    def dfs(self):
        self.vertexList[0].wasVisited = True
        self.displayVertex(0)   # pobranie wierzchołka ze szczytu
        self.theStack.push(0)   # zapisz wierzchołek na stosie
        while not self.theStack.isEmpty():
        # Pobierz nieodwiedzony wierzchołek, przyległy do szczytowego elementu stosu
            v = self.getAdjUnvisitedVertex(self.theStack.peek())
            if v == -1:   # jeżeli nie ma takiego wierzchołka
                self.theStack.pop()  # weź następny jeżeli istnieje
            else:
                self.vertexList[v].wasVisited = True
                self.displayVertex(v)  # wyświetl wierzchołek
                self.theStack.push(v)  # zapisz na stosie
        # stos pusty, procedura zakończona
        for j in range(self.nVerts):
            self.vertexList[j].wasVisited = False
        



def main(args):
    theGraph = Graph()
    theGraph.addVertex('A')  # poczatek poszukiwań
    theGraph.addVertex('B')
    theGraph.addVertex('C')
    theGraph.addVertex('D')
    theGraph.addVertex('E')

    theGraph.addEdge(0,1)
    theGraph.addEdge(1,2)
    theGraph.addEdge(0,3)
    theGraph.addEdge(3,4)
    print ("Odwiedzone wierzchołki: ")
    theGraph.dfs()   # wyszukiwanie w głąb
    print()


if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))







