from models.usuario import Usuario

usuarios = []

def listar_usuarios():
    return [vars(u) for u in usuarios]

def obter_usuario(id):
    for u in usuarios:
        if u.id == id:
            return vars(u)
    return None

def criar_usuario(dados):
    novo = Usuario(**dados)
    usuarios.append(novo)
    return vars(novo)

def atualizar_usuario(id, dados):
    for u in usuarios:
        if u.id == id:
            u.nome = dados.get("nome", u.nome)
            u.email = dados.get("email", u.email)
            u.foto = dados.get("foto", u.foto)
            return vars(u)
    return None

def obter_pontuacao(id):
    for u in usuarios:
        if u.id == id:
            return {"pontuacao": u.pontuacao}
    return None