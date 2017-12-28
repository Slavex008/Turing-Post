from src.Transicao import Transicao
from src.Estado import Estado


class Turing:
    estadoInicial = None
    estadosFinais = None
    estados = None      #conjunto de todos os estados
    transicoes = None   #conjunto de todas as transicoes
    alfabeto = None
    todosSimbolos = None    #alfabeto + simbolos auxiliares
    
    
    
    #TODO: testar se o estado inicial e os estados finais sao referencias
    #construtor da maquina de turing
    def __init__(self, estadoInicial, estadosFinais, estados, transicoes, alfabeto, todosSimbolos):
        #cria os estados e os insere no dicionario de estados
        self.estados = {}
        for e in estados:
            estado = Estado(e)
            self.estados[estado.nome] = estado
        
        #se o estado inicial nao pertencer ao conjunto de estados, gera erro
        if(estadoInicial not in self.estados):
            return None
        
        self.estadoInicial = self.estados[estadoInicial]
        
        self.estadosFinais = {}
        
        #gera o conjunto de estados finais
        for ef in estadosFinais:
            # se algum estado final nao pertencer ao conjunto de estados, gera erro
            if((ef not in self.estados) or (ef in self.estadosFinais)):
                return None
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
                return None
            alfabeto[letra] = letra
        
        self.transicoes = []
        #cria as transicoes e as insere na lista de transicoes
        for transicao in transicoes:
            #testa se ha algum valor invalido na transicao, se houver, gera erro
            if(((transicao[0] not in self.estados) or (transicao[4] not in self.estados))
                or (transicao[1] not in self.todosSimbolos) or (transicao[2] not in self.todosSimbolos)
                or ((transicao[3] != 'D') and (transicao[3] != 'E'))):
                return None
            
            self.transicoes.add(Transicao(self.estados[transicao[0]], transicao[1], transicao[2],
                                            transicao[3], self.estado[transicao[4]]))
            
        
        