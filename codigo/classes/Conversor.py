from classes.post.Post import Post
from classes.post.Leitura import Leitura
from classes.post.Escrita import Escrita
from classes.post.Desvio import Desvio


class Conversor:
    contadorID = 0
    turing = None
    post = None
    
    def __init__(self, turing):
        self.turing = turing
        self.post = Post(turing.alfabeto)
        self.incrementarContador()
        self.incrementarContador()
        for estado in self.turing.estados:
            turing.estados[estado].equivalentePost = None
        for transicao in self.turing.transicoes:
            transicao.usada = False
            
        self.converter(self.turing.estadoInicial)
        
    def converter(self, estadoAtual):
        if(estadoAtual == None):
            return None
        
        transicao = self.encontraProximaTransicao(estadoAtual)
        # se houver retorno, significa que a transicao retornada deve ser transformada para POST
        if(transicao != None):
            if(estadoAtual.equivalentePost == None):
                estadoAtual.equivalentePost = Leitura(str(self.contadorID))
            leitura = estadoAtual.equivalentePost
            self.incrementarContador()
            if(transicao.estadoOrigem == transicao.estadoDestino):
                self.criaEquivalentePost(transicao, leitura, leitura)
                self.converter(estadoAtual)
                return
            if(transicao.estadoDestino.equivalentePost == None):
                self.converter(transicao.estadoDestino)
            self.criaEquivalentePost(transicao, leitura, transicao.estadoDestino.equivalentePost)
            return
                
        self.converter(self.getOrigemTransicaoNaoUsada())
            
    
    # Cria um conjunto de desvios, leituras e escritas equivalentes a transicao
    def criaEquivalentePost(self, transicao, leitura, destinoEscrita):
        if(transicao.movimento == 'D'):
            self.criaMovimentoDireita(leitura, transicao.simboloLido, transicao.simboloEscrito,
                                      destinoEscrita)
    
    # cria o desvio e a instruçao de escrita e os adiciona, junto a leitura, a maquina de POST
    def criaMovimentoDireita(self, leitura, simboloLido, simboloEscrito, destinoEscrita):
        escrita = Escrita(str(self.contadorID), simboloEscrito, destinoEscrita)
        self.incrementarContador()
        desvio = Desvio(leitura, simboloLido, escrita)
        self.post.adicionarLeitura(leitura)
        self.post.adicionaEscrita(escrita)
        self.post.adicionarDesvio(desvio)
        
    
    # retorna a primeira transicao encontrada que ainda nao foi transformada em POST
    # e a marca como usada
    def encontraProximaTransicao(self, estado):
        for transicao in self.turing.transicoes:
            if(not(transicao.usada) and transicao.estadoOrigem == estado):
                transicao.usada = True
                return transicao
            
        return None
    
    #retorna o primeiro estado encontrado de forma que tal estado seja origem de uma transicao
    #ainda nao transformada para POST
    def getOrigemTransicaoNaoUsada(self):
        for transicao in self.turing.transicoes:
            if(not(transicao.usada)):
                return transicao.estadoOrigem
        
        return None

    def incrementarContador(self):
        self.contadorID += 1

