from classes.post.Post import Post


class Conversor:
    contadorID = 0
    turing = None
    post = None
    
    def incrementarContador(self):
        self.contadorID += 1
    
    def __init__(self, turing):
        self.turing = turing
        self.post = Post(turing.alfabeto)
        self.incrementarContador()
        self.incrementarContador()
        self.converter()
        
    def converter(self):
        return