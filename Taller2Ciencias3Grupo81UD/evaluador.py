import expresion
import variable

class Evaluador:
    def __init__(self):
        self.exps = []
    
    def txt_to_list(self):
        self.exps = ([x.split() for x in open("expresiones.txt", "r").read().split("\n")])
    #{'variable', 'expresion','value'}
    
    
    def calcular_solucion(self):
        #print (self.exps)
        datos_exp=[]
        
        
        for x in self.exps:
            llave = x[len(x)-2]
            datos_calculo = x[0:len(x)-2]
            valor=None
            datos_exp.append([llave, datos_calculo, valor]) 
            #print(llave)
            #print("datos",datos_calculo)
            
        #evaluar expresiones
        #print("Resultados: ")
        a = expresion.Expresion()
        for x in datos_exp:
            
            a.array_to_cola(x[1])
            a.calcular()
            x[2] = a.get_result()
            b=x[0]
            c=x[2]
            print(b, " = ",c)
            if (x[0]=='x'):
                a.equis.setValor(c)
                print(a.equis.getValor(),"valor x")
            elif(x[0]=='y'):
                
                a.ye.setValor(c)
                print(a.ye.getValor(),"valor x")
            elif(x[0]=='z'):
                
                a.zeta.setValor(c)
                print(a.zeta.getValor(),"valor x")
