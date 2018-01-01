class ConversaoException(Exception):
    mensagem = None
    def __init__(self, mensagem):
        self.mensagem = mensagem