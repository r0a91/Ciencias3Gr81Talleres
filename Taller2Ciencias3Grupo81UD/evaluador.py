import expresion

class Evaluador:
    def __init__(self):
        self.exps = []
    
    def txt_to_list(self):
        self.exps = ([x.split() for x in open("expresiones.txt", "r").read().split("\n")])
    #{'variable', 'expresion','value'}
    
    
    def calcular_solucion(self):
        print (self.exps)
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
        for x in datos_exp:
            a = expresion.Expresion(x[1])
            a.array_to_cola()
            a.calcular()
            x[2] = a.get_result()
            print(x[0], " = ", x[2])
			
			
			
			    
        
        


