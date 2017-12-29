# -*- coding: UTF-8 -*-
from Estado import Estado
class Transicao(object):
    estadOrigem = None
    estadoDestino = None
    simboloLido = None
    simboloEscrito = None
    movimento = None

    def __init__(self, estadoOrigem, simboloLido, simboloEscrito, movimento, estadoDestino):
        self.estadoOrigem = estadoOrigem
        self.estadoDestino = estadoDestino
        self.simboloLido = simboloLido
        self.simboloEscrito = simboloEscrito
        self.movimento = movimento
    
    