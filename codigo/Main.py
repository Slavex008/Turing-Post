# -*- coding: UTF-8 -*-
import sys
from classes.Leitor import Leitor
from classes.turing.Turing import Turing
from excecoes.CriacaoTuringException import CriacaoTuringException
from classes.Conversor import Conversor
from classes.Escritor import Escritor

from excecoes.ConvercaoException import ConversaoException


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
        Escritor(saida, conversor.post)
        
    except CriacaoTuringException as e:
        print("Ocorreu um erro na criacao da maquina de Turing")
        print(e.mensagem)
    except ConversaoException as e:
        print("Ocorreu um erro na conversao da maquina de Turing")
        print(e.mensagem)
    
main()