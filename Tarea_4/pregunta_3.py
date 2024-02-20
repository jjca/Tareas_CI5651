import sys

class indiceError(Exception):
    "Error de indice"
    pass

class negativeInteger(Exception):
    "Entero negativo"
    pass

class sizeError(Exception):
    "Entero negativo"
    pass

def verificarInicializacion(a,b,T,posicion,ctr):
    if b[posicion] != None and (0 <= b[posicion] and b[posicion] <= ctr):
        if a[b[posicion]] == posicion:
            print(f"El elemento T[{posicion}] está inicializado y vale {T[posicion]}")
            return True
        else:
            print(f"El elemento T[{posicion}] NO está inicializado")
            return False
    else:
        print(f"El elemento T[{posicion}] NO está inicializado")
        return False

def asignarValor(a,b,T,valor,posicion,ctr):
    if not verificarInicializacion(a,b,T,posicion,ctr):
        a[ctr] = posicion 
        T[posicion]= valor
        b[posicion] = ctr
        ctr+=1
        print(f"a: {a}")
        print(f"b: {b}")
        print(f"T: {T}")
        print(ctr)
        return ctr
    else:
        T[posicion] = valor
        print(f"a: {a}")
        print(f"b: {b}")
        print(f"T: {T}")
        print(ctr)
        return ctr

def main():
    nasignado = False
    while not nasignado:
        try:
            n = int(input("Por favor introduzca el tamaño del arreglo: "))
            if n <= 0:
                raise negativeInteger
            elif n >= 1000000:
                raise sizeError
            nasignado = True
        except ValueError:
            print("El valor no es un entero")
        except negativeInteger:
            print("El valor no es un entero positivo")
        except sizeError:
            print("Entero muy grande")
    a = [None]*n
    b = [None]*n
    T = [None]*n
    global ctr
    ctr = 0
    print("Introduzca el comando")
    for line in sys.stdin:
        entrada = line.rstrip().split(" ")
        if 'salir' == line.rstrip().lower():
            break
        elif len(entrada) == 3:
            if 'asignar' == entrada[0].lower():
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
                    continue

        elif len(entrada) == 2:
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
                print("Sintaxis incorrecta. Vuelva a escribir")

        elif 'limpiar' == entrada[0].lower():
            a = [None]*n
            b = [None]*n
            T = [None]*n
            ctr = 0
        else:
            print("Error de sintaxis vuelva a escribir")
    print("Saliste!")

if __name__ == "__main__":
    main()