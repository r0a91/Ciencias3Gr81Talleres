import pila
import cola
import sys
class var:
    def __init__(self,nombre="",valor=0):
        self.nombre=nombre
        self.valor=valor
    def getNombre(self):
        return self.nombre
    def getValor(self):
        return self.valor
    def setValor(self,val):
        self.valor=val
class Expresion:

    def __init__(self):
        self.lista = []
        self.Cola = cola.Cola()
        self.pila = pila.Pila()
        self.equis=var("x",1)
        self.ye=var("y",2)
        self.zeta=var("z",3)
    
    def array_to_cola(self,lista):
        self.Cola.limpiar()
        for e in lista:
            
            self.Cola.encolar(e)

    def calcular(self):
		
        if self.Cola.es_vacia():
            print("No hay mas elementos en la cola")
        else:
            dato = self.Cola.desencolar()
            #print(dato)
            if (dato == '+' or dato == '-'  or dato == '*' or dato == '/'):
                a = self.pila.desapilar()
                b = self.pila.desapilar()
                if (a=='x'):
                    a=self.equis.getValor()
                elif(a=='y'):
                    a=self.ye.getValor()
                elif(a=='z'):
                    a=self.zeta.getValor()
                if (b=='x'):
                    b=self.equis.getValor()
                elif(b=='y'):
                    b=self.ye.getValor()
                elif(b=='z'):
                    b=self.zeta.getValor()
                print(a)
                print("b ",b)
                try:
                    a = float(a)
                    
                except ValueError:
                    print("No se puede evaluar: ",a)
                    sys.exit(1)
                try:
                    b = float(b)
                    
                except ValueError:
                    print("No se puede evaluar: " ,b)
                    sys.exit(1)

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
            print("Ingreso la expresion: ", str(self.lista),"de manera erronea")
	
	
	
              
        
    

