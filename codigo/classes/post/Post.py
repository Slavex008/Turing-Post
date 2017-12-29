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
    rejeicao = Rejeita()
    aceitacao = Aceita()
    
    def __init__(self, alfabeto):
        self.alfabeto = alfabeto
        self.alfabeto['#'] = '#'
        self.partida = '0'
        self.leituras = {}
        self.escritas = {}
        self.desvios = []
        self.escritas['1'] = Escrita('1', self.alfabeto['#'], '2')
        
        
    def addComponente(self, componente):
        self.componentes[componente.id] = componente