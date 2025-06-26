class Usuario:
    def __init__(self, id, nome, email, foto):
        self.id = id
        self.nome = nome
        self.email = email
        self.foto = foto
        self.pontuacao = 0
        self.historico = []