class Atividade:
    def __init__(self, id, titulo, descricao, categoria, pontos):
        self.id = id + 1
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.pontos = pontos
        self.realizada = False
