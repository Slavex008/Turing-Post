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
        if(escrita.id == '4'):
            print("euEscrita")
        self.escritas[escrita.id] = escrita
    
    def adicionarLeitura(self, leitura):
        if (leitura.id == '4'):
            print("euLeitura")
        self.leituras[leitura.id] = leitura
    
    def adicionarDesvio(self, desvio):
        if (desvio.origem.id == '4'):
            print("euDesvio")
        self.desvios.append(desvio)
        
    