from classes.post.AceitaRejeita import Rejeita
from classes.post.AceitaRejeita import Aceita
from classes.post.Desvio import Desvio
from classes.post.Leitura import Leitura
from classes.post.Escrita import Escrita


class Post:
    alfabeto = None
    partida = None
    desvios = None
    leituras = None
    escritas = None
    identificadorEsquerda = '&' #variavel auxiliar usada para simular o movimento para a esquerda
    rejeicao = Rejeita()
    aceitacao = Aceita()
    
    def __init__(self, alfabeto):
        self.alfabeto = alfabeto
        print(alfabeto)
        self.alfabeto['#'] = '#'
        # self.alfabeto[self.identificadorEsquerda] = self.identificadorEsquerda
        self.partida = '0'
        self.leituras = {}
        self.escritas = {}
        self.desvios = []
        
    def adicionarEscrita(self, escrita):
        if(escrita.id in self.escritas):
            return
        self.escritas[escrita.id] = escrita
    
    def adicionarLeitura(self, leitura):
        if (leitura.id in self.leituras):
            return
        self.leituras[leitura.id] = leitura
        for letra in self.alfabeto:
            self.desvios.append(Desvio(self.leituras[leitura.id],
                                       letra, self.rejeicao))
    
    def adicionarDesvio(self, desvio):
        for d in self.desvios:
            if((desvio.origem.id == d.origem.id) and (desvio.simbolo == d.simbolo)):
                d.destino = desvio.destino
                return
        self.desvios.append(desvio)
        
    