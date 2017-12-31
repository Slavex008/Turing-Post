class Escritor:
    arquivo = None
    def __init__(self, arquivo, post):
        self.arquivo = open(arquivo, "w+")
        self.post = post
        self.arquivo.write(self.formataMaquina(post))
        
    def formataMaquina(self, post):
        texto = ""
        alfabeto = "{"
        for letra in post.alfabeto:
            alfabeto += letra + ", "
        
        alfabeto = alfabeto[:-1]
        alfabeto += "}"
        
        texto += alfabeto + "\n"
        
        leituras = "{\n"
        for leitura in post.leituras:
            leituras += "   (" + post.leituras[leitura].id + "), \n"
        
        leituras = leituras[:-3]
        leituras += "\n}"
        
        texto += leituras + "\n"
        
        escritas = "{\n"
        for escrita in post.escritas:
            escritas += "   (" + post.escritas[escrita].id + ", " + \
                            post.escritas[escrita].simbolo + ", " + \
                            post.escritas[escrita].destino.id + "), \n"
        
        escritas = escritas[:-3]
        escritas += "\n}"
        
        texto += escritas + "\n"
        
        desvios = "{\n"
        for desvio in post.desvios:
            desvios += "    (" + desvio.origem.id + \
                        ", " + desvio.simbolo + \
                        ", " + desvio.destino.id + "), \n"
        
        desvios = desvios[:-3]
        desvios += "\n}"
        
        texto += desvios + "\n"
        
        return texto