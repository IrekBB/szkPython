from MojeTypy import GraphSearch as gs

def main(args):
    theGraph = gs.Graph()
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
    theGraph.bfs()   # wyszukiwanie w szerz
    print()

if __name__=="__main__":
    import sys
    sys.exit(main(sys.argv))