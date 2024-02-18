import sys

class indexError(Exception):
    "Error de indice"
    pass

""" 
Clase programa que incluye los lenguajes que soporta y su nombre
"""
class Program:
    def __init__(self,name,language):
        self.name = name
        self.languages = [language]
    
    def addLanguage(self,language):
        self.languages.append(language)
    
    def getLanguages(self):
        return self.languages
    
    def getName(self):
        return self.name
    
"""
Clase interprete con el lenguaje de origen y el de destino
"""
class Interpreter:
    def __init__(self,base_language,language):
        self.base_language = base_language
        self.language = language

    def getBaseLanguage(self):
        return self.base_language
    
    def getDestLanguage(self):
        return self.language
    
"""
Clase traductor
base_language = Lenguaje en el que está escrito
origin_language = Lenguaje de origen
dest_languuage = lenguaje de destino
"""
class Translator:
    def __init__(self,base_language,origin_language,dest_language):
        self.base_language = base_language
        self.origin_language = origin_language
        self.dest_language = dest_language
    

"""
Nombre del lenguaje
"""
class Language:
    def __init__(self,name):
        self.name = name

"""
Clase de la maquina
supported_languages: lista de lenguajes soportados
executable_programs: lenguajes que se ejecutan
translators: traductores añadidos
programs: programas añadidos, no necesariamente ejecutables
interpreters: interpretes añadidos
"""
class Maquina():
    def __init__(self):
        self.supported_languages = ['local']
        self.executable_programs = []
        self.translators = [Translator('local','local','local')]
        self.programs = []
        self.interpreters = []

    """
    Busca si existe el programa
    """
    def searchProgram(self,program_name,program_language):
        print(program_name)
        print(program_language)
        if len(self.programs) == 0:
            return 0
        for prog in self.programs:
            if prog.getName() == program_name:
                if (program_language in prog.getLanguages()):
                    return 2
                else:
                    print("El programa existe pero sin ese lenguaje")
                    prog.addLanguage(program_language)
                    return -1
        else:   
            print("El programa no existe")
            return 1

    """
    Loop que se ejecuta para crear nuevos interpretes y saber que lengaujes pueden interpretarse
    """
    def interpreterLoop(self,base_language,dest_language):
        old_list = self.interpreters.copy()
        
        new_interpreter = Interpreter(base_language,dest_language)
        # Si no existe el interprete lo añadimos
        if (not self.searchInterpreter(new_interpreter)):
            #print(f"El interprete que entró ahorita se creará con {base_language} -> {dest_language}")
            """ El interprete se añade a maquina y si su lenguaje base es igual a uno soportado por la maquina entonces 
            el lenguaje de destino es soportado por la maquina """
            self.addInterpreterToMachine(new_interpreter)
            
            while old_list:
                # Se desempila un interprete de la lista vieja (la que no tiene al nuevo)
                interpreter_pop = old_list.pop(0)
            #    print(f"El interprete que se sacó tiene: {interpreter_pop.getBaseLanguage()}->{interpreter_pop.getDestLanguage()}")
            #    print(f"el interprete que se va a evaluar tiene {new_interpreter.base_language} -> {new_interpreter.getDestLanguage()}")
                # Si el lenguaje base del desempilado es igual al lenguaje de destino del nuevo  entonces
                # desempilado = (L0->L1)
                # nuevo = (L2 -> L0)
                # Y
                # el lenguaje base del nuevo pertenece a la lista de soportados
                # entonces se llama para ver si hay que crear un interprete (L2 -> L1)
                
                if (interpreter_pop.getBaseLanguage() == dest_language and base_language in self.supported_languages):
                    self.interpreterLoop(base_language,interpreter_pop.getDestLanguage())
                    self.newInterpreterWithTranslators(base_language,dest_language)
                    return True
        
                #Si el lenguaje de destino del desempilado es igual al lenguaje base del nuevo 
                #    desempilado = (L0->L1) 
                #    nuevo = (L1 -> L2)
                #    Y 
                #  el lenguaje base del desempilado pertenece a la lista de soportados
                #entonces se llama para ver si hay que crear un interprete (L0 -> L2)
                elif (interpreter_pop.getDestLanguage() == base_language and interpreter_pop.getBaseLanguage() in self.supported_languages):
                    self.interpreterLoop(interpreter_pop.getBaseLanguage(),dest_language)
                    self.newInterpreterWithTranslators(base_language,dest_language)
                    return True              
            return True
        else:
            return False

    """
    Loop para generar interpretes a partir de nuevos traductores
    """
    def newInterpreterWithTranslators(self,base_language,dest_language):
        for trans in self.translators:
            if trans.base_language in self.supported_languages and trans.origin_language == base_language:
                self.interpreterLoop(trans.dest_language,dest_language)

    """
    Loop para ejecutar por cada interprete definido
    """
    def newInterpreterWithTranslator(self,translator: Translator):
        for interp in self.interpreters:
            if interp.getBaseLanguage() == translator.origin_language and translator.base_language in self.supported_languages:
                self.interpreterLoop(translator.dest_language,interp.getDestLanguage())
    
    """
    Loop usado para generar traductores, ejecutado a definir un traductor
    """
    def translatorLoop(self,base_language,origin_language,dest_language):
        """
        base_language: lenguaje en el que esta escrito
        origin_language: lenguaje desde el cual se traudce
        dest_language: lenguaje al que se traduce
        (origin_language -> destlanguage)(base_language)
        """
        old_list = self.translators.copy()
        if (not self.searchTranslator(base_language,origin_language,dest_language)):
            print(f"Vamos a definir el traductor desde {origin_language} -> {dest_language} escrito en {base_language}")
            new_translator = self.addTranslator(base_language,origin_language,dest_language)[1]
            
            if new_translator.base_language in self.supported_languages and new_translator.dest_language in self.supported_languages:
                # Si el lenguaje en el que esta escrito el traductor lo entiende la maquina 
                # Y 
                # el lenguaje de origen lo entiende la maquina
                # Entonces el lenguaje de destino lo entiende la maquina 
                # (T1 -> T2)(T0) /\ T0 and T1 in supported_lang => T2 in supported_lang
                self.addLanguageToMachine(new_translator.origin_language)
            while old_list:
                translator_pop = old_list.pop(0)

                if (translator_pop.origin_language == new_translator.base_language):
                    # Nuevo: (T0 -> T1)(T2)
                    # POP: (T2 -> T3)(T4)
                    # Crea: (T0 -> T1)(T4)
                    # Si el Lenguaje que recibe el traductor_pop pertenece a los soportados por la maquina (T2 in supported)
                    # Y 
                    # El lenguaje en el que esta escrito el traductor_pop (T4 in supported) 
                    # ENTONCES
                    # Se debe crear el traductor desde el lenguaje de origen (T0) del nuevo traductor hacia el de destino del nuevo (T1), escrito en el de destino del traductor_pop (T3)

                    self.translatorLoop(translator_pop.dest_language,new_translator.origin_language,new_translator.dest_language)
                    self.newInterpreterWithTranslator(new_translator)
                    return True
                elif (new_translator.origin_language == translator_pop.base_language and new_translator.base_language in self.supported_languages):
                    # Nuevo: (T0 -> T1)(T2)
                    # POP: (T2 -> T3)(T4)
                    # Crea: (T0 -> T1)(T3)
                    # Si el Lenguaje de origen del traductor nuevo (T0) es igual al lenguaje en el que esta escrito el traductor pop (T4)
                    # ENTONCES
                    # Se debe crear el traductor desde el lenguaje de origen (T0) del nuevo traductor hacia el de destino del nuevo (T1), escrito en el de destino del traductor_pop (T3)
                    self.translatorLoop(new_translator.dest_language,translator_pop.origin_language,translator_pop.dest_language)
                    self.newInterpreterWithTranslator(new_translator)
                    return True
                
        else:
            return False               

    """
    Añade un programa a la maquina
    """     
    def addProgram(self,program_name,program_language):
        self.programs.append(Program(program_name,program_language))
        return True
    """
    Añade un lenguaje a un programa
    """
    def addLanguageToProgram(self,program_name,program_language):
        for prog in self.programs:
            if prog.getName() == program_name:
                prog.addLanguage(program_language)
    
    """
    Busca si existe un interprete
    """
    def searchInterpreter(self,interpreter):
        for Interp in self.interpreters:
            if Interp.base_language == interpreter.getBaseLanguage() and Interp.language == interpreter.getDestLanguage():
                print("Interpreter already exists")
                return True
        else:
            return False
        
    """
    Añade un interprete a la maquina
    """
    def addInterpreterToMachine(self,new_interpreter):
        if new_interpreter.getBaseLanguage() in self.supported_languages and new_interpreter.getDestLanguage() not in self.supported_languages:
            self.supported_languages.append(new_interpreter.getDestLanguage())
        self.interpreters.append(new_interpreter)
            
    def searchTranslator(self,base_language,origin_language,dest_language):
        for trans in self.translators:
            if trans.base_language == base_language and trans.dest_language == dest_language and trans.origin_language == origin_language:
                print("Translator already exists")
                return True
        else:
            print("Traductor no existe")
            return False
    
    # Añade un traductor
    def addTranslator(self,base_language,origin_language,dest_language):
        """
        base_language: lenguaje en el que esta escrito
        origin_language: lenguaje desde el cual se traudce
        dest_language: lenguaje al que se traduce
        """
        translator = Translator(base_language,origin_language,dest_language)
        self.translators.append(translator)
        return True,translator
    
    # Añade un lenguaje a la maquina
    def addLanguageToMachine(self,language):
        if language not in self.supported_languages:
            self.supported_languages.append(language)
            return True
        return False
    
    # Verifica si un programa es ejecutable
    def checkIfExecutable(self,program_name):
        if len(self.programs) == 0:
            return False
        for program in self.programs:
            if program_name == program.name:
                print(f"Revisando {program.getName()}")
                for lang in program.getLanguages():
                    if lang in self.supported_languages:
                        print(f"El lenguaje {lang} es soportado")
                        print(self.supported_languages)
                        return True
                print(f"El lenguaje {lang} NO es soportado")
                print(self.supported_languages)
                return False
            else: 
                print(f"{program_name}, {program.name}")
        return False
        



def asignarValor(a,b,T,valor,posicion,ctr):
    #verificarAsignado(T)
    a[ctr] = posicion 
    T[posicion]= valor
    b[posicion] = ctr
    ctr+=1
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"T: {T}")
    print(ctr)
    return ctr

def main():

    try:
        n = int(input("Por favor introduzca el tamaño del arreglo: "))
        if n <= 0:
            print("Se requieren enteros positivos")
    except ValueError:
        print("el valor no es un entero")
    if (isinstance(n,int)):
        print("Holi")
    else:
        print("Chao")
    a = [None]*n
    b = [None]*n
    T = [None]*n
    global ctr
    ctr = 0
    for line in sys.stdin:
        entrada = line.rstrip().split(" ")
        if 'salir' == line.rstrip().lower():
            break
        elif len(entrada) == 3:
            if 'asignar' == entrada[0].lower():
                try:
                    posicion = int(entrada[1])
                    valor = int(entrada[2])
                    print(f"posicion: {posicion}")
                    print(f"valor: {valor}")
                    print(f"n vale: {n}")
                    if 0 > posicion or posicion >= n:
                        print(f"El valor {posicion} no está en el rango [0,{n-1}]")
                        raise indexError("Error de indice")
                    ctr = asignarValor(a,b,T,valor,posicion,ctr)
                except ValueError:
                    print("Alguno de los valores introducidos no es un número")

        elif len(entrada) == 2:
            if 'consultar' == entrada[0].lower():
                try:
                    posicion = int(entrada[1])
                    if isinstance(posicion, int) and posicion >= 0:
                        if posicion >= n:
                            print("Error de índice")
                except ValueError:
                    print("no son numeros")    
            else:
                print("Sintaxis incorrecta. Vuelva a escribir")

        elif 'ejecutable' == entrada[0].lower():
            print(f"El nombre del programa es: {entrada[1]}")
            if (LOCAL.checkIfExecutable(entrada[1].lower())):
                print(f"El programa {entrada[1]} es ejecutable")
            else:
                print(f"El programa {entrada[1]} no es ejecutable")
        else:
            print("Error de sintaxis vuelva a escribir")
    print("Exit")

if __name__ == "__main__":
    main()