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
    def __init__(self, val):
        self.val = val
        self.weight = random.randint(0, 99)
        self.size = 1
        self.left = None
        self.right = None

    def __str__(self):
        if not self:
            return ""
        return str(self.left) + str(self.val) + str(self.right)

class Treap:

    def __init__(self):
        self.root = None

    def size(self,node: Node):
        if node is not None:
            return node.size
        else:
            return 0
        # Codigo extraido de Geeks for Geeks  https://www.geeksforgeeks.org/implementation-of-search-insert-and-delete-in-treap/
            
    def split(self, treap, val):
        if (treap is None):
            return (None,None)

        if (val > self.size(treap)):
            l,treap.left = self.split(treap.left,val)
            r = treap
        else:
            treap.right, r = self.split(treap.right,val-self.size(treap.left)-1)
            l = treap
        treap.size = 1 + self.size(treap.left) + self.size(treap.right)
        return (l,r)
        

    def merge(self, left:Node, right:Node):
        if left == None:
            return right
        
        elif right == None:
            return left
        
        elif left.weight < right.weight:
            left.right = self.merge(left.right,right)
            treap = left 
        else:
            right.left = self.merge(left,right.left)
            treap = right
        treap.size = 1 + self.size(treap.left) + self.size(treap.right)
        return treap

    def find(self,t,val):
        if t == None:
            return None
        if t.weight == val:
            return t
        elif val < t.weight:
            return self.find(t.left,val)
        else:
            return self.find(t.right,val)

    def insert(self,val):
        node = Node(val)
        node.size = self.size(node)
        if self.root == None:
            self.root = node
            return
        L,R = self.split(self.root,node.size)
        self.root = self.merge(L,node)
        self.root = self.merge(self.root,R)

    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print("val:", node.val, "| priority:", node.weight, self.size(node), end="")
            if node.left:
                print(" | left child:", node.left.val, end="")
            if node.right:
                print(" | right child:", node.right.val, end="")
            print()
            self.inorder(node.right)

    def multiswap(self,a,b):
        node = self.find(self.root,a)
        L,R = self.split(node,a)
        
        self.inorder(L)
        print(node)
        self.inorder(R)
        #self.root = self.merge(L,node)
        #self.root = self.merge(R,node)
        print("exitoso")
        
# Codigo extraido de https://gist.github.com/IvanIsCoding/0abbe10dc8dc7cf330e410cf49875593
# Codigo extraido de Geeks for Geeks  https://www.geeksforgeeks.org/implementation-of-search-insert-and-delete-in-treap/

# A utility function to print tree


A = [1,2,3,4,5,6,7,8,9,10]
random.seed(2)
arbol = Treap()
for i in range(0,len(A)):
    arbol.insert(A[i])

arbol.inorder(arbol.root)
print(arbol.size(arbol.root))

arbol.multiswap(2,5)
#arbol.inorder(arbol.root)

B = multiswap(A,2,5)


#B = multiswap(A,2,3)
print(B)