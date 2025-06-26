from models.historico import HistoricoAtividade

historicos = []

def listar_historico():
    return [vars(h) for h in historicos]

def listar_por_usuario(usuario_id):
    return [vars(h) for h in historicos if h.usuario_id == usuario_id]

def registrar_atividade(dados):
    novo = HistoricoAtividade(**dados)
    historicos.append(novo)
    return vars(novo)

def atualizar_historico(id, dados):
    for h in historicos:
        if h.id == id:
            h.feita = dados.get("feita", h.feita)
            h.salva = dados.get("salva", h.salva)
            return vars(h)
    return None
def deletar_historico(id):
    global historicos
    for h in historicos:
        if h.id == id:
            historicos = [x for x in historicos if x.id != id]
            return True
    return False
