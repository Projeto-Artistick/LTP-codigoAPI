from flask import Blueprint, request, jsonify
from services import usuario_service

usuario_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")

@usuario_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(usuario_service.listar_usuarios())

@usuario_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    u = usuario_service.obter_usuario(id)
    if u:
        return jsonify(u)
    return jsonify({"erro": "Usuário não encontrado"}), 404

@usuario_bp.route("/", methods=["POST"])
def create():
    dados = request.json
    return jsonify(usuario_service.criar_usuario(dados)), 201

@usuario_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    dados = request.json
    atualizado = usuario_service.atualizar_usuario(id, dados)
    if atualizado:
        return jsonify(atualizado)
    return jsonify({"erro": "Usuário não encontrado"}), 404

@usuario_bp.route("/<int:id>/pontuacao", methods=["GET"])
def get_score(id):
    pontuacao = usuario_service.obter_pontuacao(id)
    if pontuacao:
        return jsonify(pontuacao)
    return jsonify({"erro": "Usuário não encontrado"}), 404

@usuario_bp.route("/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    sucesso = usuario_service.deletar_usuario(id)
    if sucesso:
        return "", 204
    return jsonify({"erro": "Usuário não encontrado"}), 404