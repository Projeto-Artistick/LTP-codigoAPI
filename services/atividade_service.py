from models.atividade import Atividade

atividades = []

def listar_atividades():
    return [vars(a) for a in atividades]

def obter_atividade(id):
    for a in atividades:
        if a.id == id:
            return vars(a)
    return None

def criar_atividade(dados):
    nova = Atividade(**dados)
    atividades.append(nova)
    return vars(nova)

def atualizar_atividade(id, dados):
    for a in atividades:
        if a.id == id:
            a.titulo = dados.get("titulo", a.titulo)
            a.descricao = dados.get("descricao", a.descricao)
            a.categoria = dados.get("categoria", a.categoria)
            a.pontos = dados.get("pontos", a.pontos)
            a.realizada = dados.get("realizada", a.realizada)
            return vars(a)
    return None

def deletar_atividade(id):
    global atividades
    atividades = [a for a in atividades if a.id != id]
    return True