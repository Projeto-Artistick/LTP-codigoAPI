class HistoricoAtividade:
    def __init__(self, id, usuario_id, atividade_id, feita=False, salva=False):
        self.id = id
        self.usuario_id = usuario_id
        self.atividade_id = atividade_id
        self.feita = feita
        self.salva = salva