class Desvio:
    origem = None
    simbolo = None
    destino = None
    
    def __init__(self, origem, destino, simbolo):
        self.origem = origem
        self.destino = destino
        
    def __eq__(self, other):
        if((self.origem.id == other.origem.id)
            and (self.simbolo == other.simbolo)
            and (self.destino == other.destino)):
            return True
        
        return False