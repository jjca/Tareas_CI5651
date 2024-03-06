import random 

def swap(A,i,j):
    #print(A)
    A[j], A[i] = A[i], A[j]
    #print(A)
    return A

def multiswap(A, a, b):
    i = a
    j = b
    while (i < b and j <= len(A)-1):
        #print(A)
        A = swap(A,i,j)
        i += 1
        j += 1
    #print(A)
    return A
 
# Definicion de clase nodo - Basado en codigo de GFG
class Node:
    def __init__(self, key):
        self.key = key
        self.weight = random.randint(0, 99)
        self.size = 1
        self.left = None
        self.right = None

    def __str__(self):
        if not self:
            return ""
        return str(self.left) + str(self.key) + str(self.right)

class Treap:

    def __init__(self):
        self.root = None

    def size(treap: Node):
        if treap is not None:
            return treap.size
        else:
            return 0
        # Codigo extraido de Geeks for Geeks  https://www.geeksforgeeks.org/implementation-of-search-insert-and-delete-in-treap/
            
    def split(self,treap, key):
        if (treap is None):
            return (None,None)

        if (key < treap.key):
            l,treap.left = self.split(treap.left,key)
            r = treap
            return (l,r)
        else:
            treap.right, r = self.split(treap.right,key)
            l = treap
            return (l,r)
        treap.size = 1 + size(treap.left) + size(treap.right)

    def merge(self, left:Node, right:Node):
        if left == None:
            return right
        elif right == None:
            return left
        elif left.weight > right.weight:
            left.right = self.merge(left.right,right)
            return left
        else:
            right.left = self.merge(left,right.left)
            return right

    def insert(self,key):
        node = Node(key)
        if self.root == None:
            self.root = node
            return
        print(node)
        L,R = self.split(self.root,key-1)
        self.root = self.merge(L,node)
        self.root = self.merge(self.root,R)

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print("key:", root.key, "| priority:", root.weight, end="")
            if root.left:
                print(" | left child:", root.left.key, end="")
            if root.right:
                print(" | right child:", root.right.key, end="")
            print()
            self.inorder(root.right)
        
# Codigo extraido de https://gist.github.com/IvanIsCoding/0abbe10dc8dc7cf330e410cf49875593
# Codigo extraido de Geeks for Geeks  https://www.geeksforgeeks.org/implementation-of-search-insert-and-delete-in-treap/

# A utility function to print tree


A = [1,2,3,4,5,6]

arbol = Treap()
for i in range(0,len(A)):
    arbol.insert(A[i])

arbol.inorder(arbol.root)

B = multiswap(A,0,4)
#B = multiswap(A,2,3)
print(B)