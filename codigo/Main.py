# -*- coding: UTF-8 -*-
import sys
from classes.Leitor import Leitor
from classes.turing.Turing import Turing
from excecoes.CriacaoTuringException import CriacaoTuringException
from classes.Conversor import Conversor
from classes.Escritor import Escritor


def main():
    try:
        if(len(sys.argv) != 3):
            print("Modo de execucao: ./Main.py <arquivo-de-entrada> <arquivo-de-saida>")
            print("Obs: O arquivo de entrada deve estar no diretorio \"arquivos/estradas\" "
                   + "deste projeto")
            return
        
        entrada = "../arquivos/entradas/" + sys.argv[1]
        saida = "../arquivos/saidas/" + sys.argv[2]
    
        leituraMT = Leitor(entrada)
        
        mt = Turing(leituraMT.estadoInicial, leituraMT.estadosFinais, leituraMT.estados,
                           leituraMT.transicoes, leituraMT.alfabeto, leituraMT.todosSimbolos)
        
        conversor = Conversor(mt)
        escritor = Escritor(saida, conversor.post)
        
        
        # print("Estados:")
        # for estado in mt.estados:
        #     print(mt.estados[estado])
        #     print(mt.estados[estado].nome)
        #
        # print()
        #
        # print("Estado inicial:")
        # print(mt.estadoInicial)
        # print(mt.estadoInicial.nome)
        # print()
        #
        # print("Estados finais:")
        # for estado in mt.estadosFinais:
        #     print(mt.estadosFinais[estado])
        #     print(mt.estadosFinais[estado].nome)
        #
        # print()
        # print("Alfabeto")
        # print(mt.alfabeto)
        # print("Todos os simbolos:")
        # print(mt.todosSimbolos)
        # print()
        #
        # print("Transicoes:")
        # for t in mt.transicoes:
        #     print(t.estadoOrigem)
        #
    except CriacaoTuringException as cte:
        print("Ocorreu um erro na criacao da maquina de Turing")
        print(cte.mensagem)
        
    
main()