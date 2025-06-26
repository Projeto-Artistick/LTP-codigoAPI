from models.usuario import Usuario

usuarios = []

contador_usuario_id = 0

def gerar_usuario_id():
    global contador_usuario_id
    contador_usuario_id += 1
    return contador_usuario_id

def listar_usuarios():
    return [vars(u) for u in usuarios]

def obter_usuario(id):
    for u in usuarios:
        if u.id == id:
            return vars(u)
    return None

def criar_usuario(dados):
    novo = Usuario(gerar_usuario_id(), **dados)
    usuarios.append(novo)
    return vars(novo)

def atualizar_usuario(id, dados):
    for u in usuarios:
        if u.id == id:
            u.nome = dados.get("nome", u.nome)
            u.email = dados.get("email", u.email)
            u.foto = dados.get("foto", u.foto)
            print (u)
            return vars(u)
    return None

def obter_pontuacao(id):
    for u in usuarios:
        if u.id == id:
            return {"pontuacao": u.pontuacao}
    return None

def deletar_usuario(id):
    global usuarios
    for u in usuarios:
        if u.id == id:
            usuarios = [x for x in usuarios if x.id != id]
            return True
    return False