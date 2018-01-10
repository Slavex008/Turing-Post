# -*- coding: UTF-8 -*-
class Estado:
    nome = None

    def __init__(self, nome):
        self.nome = nome
    
    def __eq__(self, other):
        if(other == None):
            return False
        if(self.nome == other.nome):
            return True
        return False