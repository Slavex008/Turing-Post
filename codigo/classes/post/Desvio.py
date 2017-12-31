class Desvio:
    origem = None
    simbolo = None
    destino = None
    
    def __init__(self, origem, simbolo, destino):
        self.origem = origem
        self.destino = destino
        self.simbolo = simbolo
        
    def __eq__(self, other):
        if(other == None):
            return False
        
        if((self.origem.id == other.origem.id)
            and (self.simbolo == other.simbolo)
            and (self.destino.id == other.destino.id)):
            return True
        
        return False