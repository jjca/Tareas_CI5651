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
            yield suc

    def hasSuccessors(self,player):
        if (len(self.availablePos(player)) > 0):
            return True
        return False 

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
            return True
        count = 0
        col = []
        for i in range(0,3):
            col.append(self.board[colNum+i*3])
        for i in col:
            if i == "+":
                count+= 1
        if count == 3:
            return True
        if self.board[0] == "+" and self.board[4] == "+" and self.board[8] == "+":
            return True
        elif self.board[2] == "+" and self.board[4] == "+" and self.board[6] == "+":
            return True
        return False
    
    def evaluate(self,player):
        if (self.checkWinner()):
            if player == Primer_Jugador:
                return -1
            elif player == Segundo_Jugador:
                return 1
        else:
            return 0
        
def primero(nodo,depth, alfa, beta):
    
    if depth == 0 or not nodo.hasSuccessors(Primer_Jugador):
        return nodo.evaluate(Primer_Jugador)

    else:
        mejor = -inf
        succ = nodo.successors(Primer_Jugador)
        for i in succ:               
            mejor = max(mejor,segundo(i,depth-1,alfa,beta))
            alfa = max(alfa,mejor)
            if beta <= alfa:
                break
        return mejor

def segundo(nodo,depth,alfa,beta):
    
    if depth == 0 or not nodo.hasSuccessors(Segundo_Jugador):
        return nodo.evaluate(Segundo_Jugador)
    
    else:
        mejor = inf
        succ = nodo.successors(Segundo_Jugador)
        for i in succ:
            mejor = min(mejor,primero(i,depth-1,alfa,beta))
            beta = min(beta,mejor)
            if beta <= alfa:
                break
        return mejor

def main():
    base = [" "," "," "," "," "," "," "," "," "]
    raiz = Node(None,base,0,None)
    alfa = -inf
    beta = inf
    depth = 100

    print(segundo(raiz,depth,alfa,beta))

if __name__ == "__main__":
    main()