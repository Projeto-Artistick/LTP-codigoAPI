class Atividade:
    def __init__(self, id, titulo, descricao, categoria, pontos):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.pontos = pontos
        self.guardar = False
        self.realizada = False
