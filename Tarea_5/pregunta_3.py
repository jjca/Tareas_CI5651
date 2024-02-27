import sys, random
from math import inf,floor

global n
n = 0
Primer_Jugador = "|"
Segundo_Jugador = "-"
class Node:
    def __init__(self,parent,board,value,pos):
        self.parent = parent
        self.board = board
        self.value = value
        self.modPosition = pos

    def __repr__(self):
        return f"{self.board} - {self.value} <-> {self.parent.value}"
    
    def getBoard(self):
        tablero = self.board
        for i in range(0,9,3):
            print(f" {tablero[i]} | {tablero[i+1]} | {tablero[i+2]}")
            if i == 0 or i == 3:
                print("-----------")

    def successors(self,player):
        global n
        successors = []
        availablePos = self.availablePos(player)
        for i in availablePos:
            board = self.board[:]
            if board[i] == " ":
                board[i] = player
            elif board[i] == "-" and player == Primer_Jugador:
                board[i] = "+"
            elif board[i] == "|" and player == Segundo_Jugador:
                board[i] = "+"
            n = n+1
            val = n
            suc = Node(parent=self,board=board,value=val,pos=i)
            successors.append(suc)
        return successors


    def availablePos(self,player):
        available = []
        for x in enumerate(self.board):
            if player == "-" and self.modPosition != x[0]:
                if x[1] == " " or x[1] == "|":
                    available.append(x[0])
            if player == "|" and self.modPosition != x[0]:
                if x[1] == " " or x[1] == "-":
                    available.append(x[0])
        return available

    def checkWinner(self):
        print(f"Verificando la posicion {self.modPosition}")
        position = self.modPosition
        rowNum = floor(position/3)
        colNum = position % 3
        row = self.board[rowNum*3:(rowNum+1)*3]
        # Check row
        count = 0
        for i in row:
            if i == "+":
                count+= 1
        if count == 3:
            print(f"La fila ganadora: {row}")
            return True
        count = 0
        col = []
        for i in range(0,3):
            col.append(self.board[colNum+i*3])
        for i in col:
            if i == "+":
                count+= 1
        if count == 3:
            print(f"La columna ganadora: {col}")
            return True
        if self.board[0] == "+" and self.board[4] == "+" and self.board[8] == "+":
            return True
        elif self.board[2] == "+" and self.board[4] == "+" and self.board[6] == "+":
            return True
        return False
    
    def evaluate(self,symbol):
        if (self.checkWinner()):
            if symbol == "|":
                return -1
            else:
                return 1

        else:
            return 0
        
def primero(nodo,depth, alfa, beta):
    succ = nodo.successors(Primer_Jugador)
    if depth == 0 or len(succ) == 0:
        nodo.getBoard()
        print(nodo)
        return nodo.evaluate(symbol)

    else:
        mejor = -inf
        if symbol == "-":
                symbol = "|"    
        else:
            symbol = "-"
        for i in succ:               
            mejor = max(mejor,segundo(i,depth-1,alfa,beta))
            alfa = max(alfa,mejor)
            if beta <= alfa:
                break
        return mejor

def segundo(nodo,depth,alfa,beta):
    succ = nodo.successors(Segundo_Jugador)
    if depth == 0 or len(succ) == 0:
        nodo.getBoard()
        print(nodo)
        return nodo.checkWinner()
    
    else:
        mejor = inf
        if symbol == "-":
            symbol = "|"
        else:
            symbol = "-"
        for i in succ:
            mejor = min(mejor,primero(i,depth-1,alfa,beta,symbol))
            beta = min(beta,mejor)
            if beta <= alfa:
                break
        return mejor


""" class LaVieja:
    def __init__(self):
        self.board = [" "," "," "," "," "," "," "," "," "]

    def doMovement(self,position,symbol):
        if self.board[position] == " ":
            self.board[position] = symbol
            if self.checkWinner(position,symbol):
                return True
        elif self.board[position] == "-" and symbol == "|":
            self.board[position] = "+"
            if self.checkWinner(position,symbol):
                return True
        elif self.board[position] == "|" and symbol == "-":
            self.board[position] = "+"
            if self.checkWinner(position,symbol):
                return True
        self.printBoard()
        return False
        
    
    def checkWinner(self,position,symbol):
        rowNum = floor(position/3)
        colNum = position % 3
        row = self.board[rowNum*3:(rowNum+1)*3]
        # Check row
        count = 0
        for i in row:
            if i == "+":
                count+= 1
        if count == 3:
            print(f"La fila ganadora: {row}")
            print(f"Gano {symbol} 0")
            return True
        count = 0
        col = []
        for i in range(0,3):
            col.append(self.board[colNum+i*3])
        for i in col:
            if i == "+":
                count+= 1
        if count == 3:
            print(f"La columna ganadora: {col}")
            print(f"Gano {symbol} 1")
            return True
        if self.board[0] == "+" and self.board[4] == "+" and self.board[8] == "+":
            print(f"Gano {symbol} 2")
            return True
        elif self.board[2] == "+" and self.board[4] == "+" and self.board[6] == "+":
            print(f"Gano {symbol} 3")
            return True
        return False

    
    def availableStates(self,symbol):
        available = []
        for x in enumerate(self.board):
            if symbol == "-":
                if x[1] == " " or x[1] == "|":
                    available.append(x[0])
            if symbol == "|":
                if x[1] == " " or x[1] == "-":
                    available.append(x[0])
        print(f"Disponibles para el {symbol}: {available}")
        return available
    
    def emptyPos(self):
        return ' ' in self.board
       
    def printBoard(self):
        for i in range(0,9,3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i == 0 or i == 3:
                print("-----------")
        print("===========")

    def getMoves(self,symbol):
        return random.choice(self.availableStates(symbol)) """
    

# Un tablero es un arreglo de largo 9 con 4 posibles valores, +, -, | o " " (espacio en blanco).



def main():
    base = [" "," "," "," "," "," "," "," "," "]
    raiz = Node(None,base,0,None)
    alfa = -inf
    beta = inf
    depth = 20

    """ suc = raiz.successors("-")
    for i in suc:
        print("================")
        print(i)
        i.getBoard()
    suc_1 = suc[0].successors("|")
    for j in suc_1:
        print("================")
        print(j)
        j.getBoard()
    suc_1_2 = suc_1[0].successors("-")
    for j in suc_1_2:
        print("================")
        print(j)
        j.getBoard()
    suc_1_2_3 = suc_1_2[0].successors("|")
    for j in suc_1_2_3:
        print("================")
        print(j)
    
            j.getBoard()  """
    print(primero(raiz,depth,alfa,beta))


    

if __name__ == "__main__":
    main()
    

