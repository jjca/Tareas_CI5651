import random

random.seed(5)
def BTest(a,n):
    s = 0
    t = n-1
    print(f"estamos viendo a {a}")
    while (True):
        s = s+1
        t = t//2
        print(f"el valor de t es {t}, el de s {s}")
        if (t % 2 == 1):
            break
    x = pow(a,t,n)
    print(f"x vale: {x}")
    if x == 1 or x == n-1:
        return True
    print(s)
    for _ in range(0,s):
        x = pow(x,2,n)
        print(f"x vale: {x} potencia")
        if x == n-1:
            return True
    return False

def millRab(n):
    a = int(random.uniform(2,n-2))
    return BTest(a,n)

def millRabRep(n,k):
    for i in range(0,k):
        print(f"I vale: {i}")
        if not millRab(n):
            return False
    return True

print(millRabRep(141025414102541410253,10))