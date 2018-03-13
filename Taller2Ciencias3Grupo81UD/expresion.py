import pila
import cola
class Expresion:

    def __init__(self, lista):
        self.lista = lista
        self.Cola = cola.Cola()
        self.pila = pila.Pila()
    
    def array_to_cola(self):
        for e in self.lista:
            
            self.Cola.encolar(e)

    def calcular(self):
		
        if self.Cola.es_vacia():
            print("No hay mas elementos en la cola")
        else:
            dato = self.Cola.desencolar()
            print(dato)
            if (dato == '+' or dato == '-'  or dato == '*' or dato == '/'):
                a = self.pila.desapilar()
                b = self.pila.desapilar()
                try:
                    a = float(a)
                    print(a)
                except ValueError:
                    print(a, "No es esta calculado")
                try:
                    b = float(b)
                    print(b)
                except ValueError:
                    print(b, "No esta calculado")
                if dato == '+':
                    r = b+a
                    self.pila.apilar(r)
                    self.calcular()
                elif dato == '-':
                    r = b-a
                    self.pila.apilar(r)
                    self.calcular()
                elif dato == '*':
                    r = b*a
                    self.pila.apilar(r)
                    self.calcular()
                elif dato == '/':
                    r = b/a
                    self.pila.apilar(r)
                    self.calcular()
            else:
                self.pila.apilar(dato)
                self.calcular()
    def get_result(self):
        if (self.pila.obtener_num_elems() == 1):
            return self.pila.desapilar()
        else:
            for i in self.pila.items:
                print(i)
                print("Ingreso la expresion: ", str(self.lista),
                      "de manera erronea")
	
	
	
              
        
    

