# -*- coding: UTF-8 -*-
import sys

from Leitor import Leitor

def main():
    if(len(sys.argv) != 3):
        print("Modo de execucao: ./Main.py <arquivo-de-entrada> <arquivo-de-saida>")
        print("Obs: O arquivo de entrada deve estar no diretorio \"arquivos/estradas\" "
               + "deste projeto")
        return
    
    entrada = "../arquivos/entradas/" + sys.argv[1]
    saida = "../arquivos/saidas/" + sys.argv[2]

    leituraMT = Leitor(entrada)
    
    print(leituraMT.estados)
    print(leituraMT.estadoInicial)
    print(leituraMT.estadosFinais)
    print(leituraMT.alfabeto)
    print(leituraMT.todosSimbolos)
    for t in leituraMT.transicoes:
        print(t)
    
main()