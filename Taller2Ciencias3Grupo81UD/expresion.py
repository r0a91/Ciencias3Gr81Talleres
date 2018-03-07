import pila
import cola
class Expresion:

    def __init__(self, lista):
        self.lista = lista
        self.expre = cola.Cola()
        self.pila = pila.Pila()
    
    def array_to_cola(self):
        for e in self.lista:
            self.expre.encolar(e)

    def calcular(self):
        if self.expre.es_vacia():
            print("No hay mas elementos en la cola")
        else:
            dato = self.expre.desencolar()
            if (dato == '+' or dato == '-'  or dato == '*' or dato == '/'):
                if dato == '+':
                    a = self.pila.desapilar()
                    b = self.pila.desapilar()
                    r = b+a
                    self.pila.apilar(r)
                elif dato == '-':
                    a = self.pila.desapilar()
                    b = self.pila.desapilar()
                    r = b-a
                    self.pila.apilar(r)
                elif dato == '*':
                    a = self.pila.desapilar()
                    b = self.pila.desapilar()
                    r = b*a
                    self.pila.apilar(r)
                elif dato == '/':
                    a = self.pila.desapilar()
                    b = self.pila.desapilar()
                    r = b/a
                    self.pila.apilar(r)
                else:
                    self.pila.apilar(float(dato))
                self.calcular()
        
    

