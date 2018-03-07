import expresion

class Evaluador:
    def __init__(self):
        self.exps = []
    
    def txt_to_list(self):
        self.exps = ([x.split() for x in open("expresiones.txt", "r").read().split("\n")])
    #{'variable', 'expresion','value'}
    def calcular_solucion(self):
        
        variables = {}
        math_exps = []
        
        for x in self.exps:


            llave = x[len(x) - 2]
            datos_calulo = x[:len(x)-2]

            
            math_exps.append(datos_calulo)
            #print(llave)
            #print(datos_calulo)
        
        print(math_exps)


