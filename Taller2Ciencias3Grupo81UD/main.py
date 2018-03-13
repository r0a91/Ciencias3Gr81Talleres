import evaluador
import variable

if __name__=="__main__":
    listaVar=[]
    #equis=variable.Variable("x",9)
    a = evaluador.Evaluador()
    a.txt_to_list()
    print(a.exps)
    a.calcular_solucion()

#main()
