# -*- coding: UTF-8 -*-

from classes.turing.Transicao import Transicao
from classes.turing.Estado import Estado

from excecoes.CriacaoTuringException import CriacaoTuringException


class Turing:
    estadoInicial = None
    estadosFinais = None
    estados = None      #conjunto de todos os estados
    transicoes = None   #conjunto de todas as transicoes
    alfabeto = None
    todosSimbolos = None    #alfabeto + simbolos auxiliares
    
    
    
    #TODO: testar se o estado inicial e os estados finais sao referencias
    #construtor da maquina de turing
    def __init__(self, estadoInicial, estadosFinais, estados,
                 transicoes, alfabeto, todosSimbolos):
        
        #cria os estados e os insere no dicionario de estados
        self.estados = {}
        for e in estados:
            estado = Estado(e)
            self.estados[estado.nome] = estado
        
        #se o estado inicial nao pertencer ao conjunto de estados, gera erro
        if(estadoInicial not in self.estados):
            raise CriacaoTuringException("ERRO: O estado inicial nao esta contido " +
                                         "nos estados definidos")
        
        self.estadoInicial = self.estados[estadoInicial]
        
        self.estadosFinais = {}
        
        #gera o conjunto de estados finais
        for ef in estadosFinais:
            # se algum estado final nao pertencer ao conjunto de estados, gera erro
            if((ef not in self.estados) or (ef in self.estadosFinais)):
                raise CriacaoTuringException("ERRO: Algum estado final nao " +
                                             "esta contido nos estados definidos")
            self.estadosFinais[ef] = self.estados[ef]

        #cria um dicionario com os simbolos de entrada da MT
        self.todosSimbolos = {}
        for simbolo in todosSimbolos:
            self.todosSimbolos[simbolo] = simbolo

        #cria um dicionario com o alfabeto de entrada da MT
        self.alfabeto = {}
        for letra in alfabeto:
            #se o alfabeto nao for um subconjunto de todos os simbolos, gera erro
            if(letra not in self.todosSimbolos):
                raise  CriacaoTuringException("ERRO: Algum simbolo do alfabeto nao " +
                                              "foi inserido no conjunto de todos os simbolos")
            self.alfabeto[letra] = letra
        self.transicoes = []
        #cria as transicoes e as insere na lista de transicoes
        for transicao in transicoes:
            #testa se ha algum valor invalido na transicao, se houver, gera erro
            if(((transicao[0] not in self.estados) or (transicao[4] not in self.estados))
                or (transicao[1] not in self.todosSimbolos)
                or (transicao[2] not in self.todosSimbolos)
                or ((transicao[3] != 'D') and (transicao[3] != 'E'))):
                raise CriacaoTuringException("ERRO: Alguma transiçao nao esta definida " +
                                             "corretamente!")
            
            self.transicoes.append(Transicao(self.estados[transicao[0]], transicao[1],
                                             transicao[2], transicao[3],
                                             self.estados[transicao[4]]))
            
        