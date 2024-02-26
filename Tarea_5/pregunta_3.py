import sys
from math import inf,floor

""" class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.adyList = []

    def addNode(self,node):
        self.nodes.append(node)
        self.adyList.insert(node.parent.value,node)
    
    def addEdge(self,node1,node2):
        pass

class Node:
    def __init__(self,parent,value):
        self.parent = parent
        self.value = value
        self.board = [" "," "," "," "," "," "," "," "," "]

    def __repr__(self):
        return f"{self.value}"
    
    def getBoard(self):
        tablero = self.board
        for i in range(0,9,3):
            print(f" {tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
            if i == 0 or i == 3:
                print("-----------")

class Edge:
    def __init__(self,x,y,pos,symbol):
        self.x = x
        self.y = y
        self.action = {"pos":pos,"symbol":symbol}
        
    def __repr__(self):
        return f"{self.x}<->{self.y}" """

class LaVieja:
    def __init__(self):
        self.board = [" "," "," "," "," "," "," "," "," "]

    def doMovement(self,position,symbol):
        if self.board[position] == " ":
            self.board[position] = symbol
        else:
            print("Posicion ocupada")
        self.checkWinner(position,symbol)
        self.printBoard()
    
    def checkWinner(self,position,symbol):
        rowNum = floor(position/3)
        colNum = position % 3
        # Check row
        print(f"fila {rowNum}")
        print(f"columna {colNum}")
        
    
    def availableStates(self):
        available = []
        for i in self.board:
            if i == " ":
                available.append[i]
        print(available)
        return available
       

    def printBoard(self):
        print(self.availableStates)
        for i in range(0,9,3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i == 0 or i == 3:
                print("-----------")

# Un tablero es un arreglo de largo 9 con 4 posibles valores, +, -, | o " " (espacio en blanco).
    



def main():
    listaAdyacencias = []
    #grafo = Graph()
    #raiz = node(None,0)
    #listaAdyacencias.append(raiz)
    viejita = LaVieja()
    print("Empiezan las X. Indique una posición")
    viejita.printBoard()
    for line in sys.stdin:
        entrada = line.rstrip().split(" ")
        if 'salir' == line.rstrip().lower():
            break
        elif len(entrada) == 2:
            viejita.doMovement(int(entrada[0]),entrada[1])
            """ if 'asignar' == entrada[0].lower():
                try:
                    posicion = int(entrada[1])
                    valor = int(entrada[2])
                    print(f"La posicion es: {posicion} y el valor es: {valor}")
                    if 0 > posicion or posicion >= n:
                        print(f"El valor {posicion} no está en el rango [0,{n-1}]")
                        raise indiceError
                    else:
                        ctr = asignarValor(a,b,T,valor,posicion,ctr)
                except ValueError:
                    print("Alguno de los valores introducidos no es un número")
                except indiceError:
                    continue """

            """ elif len(entrada) == 2:
            if 'consultar' == entrada[0].lower():
                try:
                    posicion = int(entrada[1])
                    if 0 > posicion or posicion >= n:
                        print(f"El valor {posicion} no está en el rango [0,{n-1}]")
                        raise indiceError
                    else:
                        verificarInicializacion(a,b,T,posicion,ctr)
                except ValueError:
                    print("Error de sintaxis en argumentos. No son números")
                except indiceError:
                    continue
            else:
                print("Sintaxis incorrecta. Vuelva a escribir") """

            """ elif 'limpiar' == entrada[0].lower():
            a = [None]*n
            b = [None]*n
            T = [None]*n
            ctr = 0 """
        else:
            print("Error de sintaxis vuelva a escribir")
    print("Saliste!")

if __name__ == "__main__":
    main()
    

