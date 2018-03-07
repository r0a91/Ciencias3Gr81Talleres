import evaluador

def main():
    a = evaluador.Evaluador()
    a.txt_to_list()
    print(a.exps)
    a.calcular_solucion()

main()
