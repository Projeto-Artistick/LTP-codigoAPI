from flask import Blueprint, request, jsonify
from services import historico_service

historico_bp = Blueprint("historico", __name__, url_prefix="/historico")

@historico_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(historico_service.listar_historico())

@historico_bp.route("/<int:usuario_id>", methods=["GET"])
def get_by_usuario(usuario_id):
    return jsonify(historico_service.listar_por_usuario(usuario_id))

@historico_bp.route("/", methods=["POST"])
def create():
    dados = request.json
    return jsonify(historico_service.registrar_atividade(dados)), 201

@historico_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    dados = request.json
    atualizado = historico_service.atualizar_historico(id, dados)
    if atualizado:
        return jsonify(atualizado)
    return jsonify({"erro": "Histórico não encontrado"}), 404
@historico_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    sucesso = historico_service.deletar_historico(id)
    if sucesso:
        return "", 204
    return jsonify({"erro": "Histórico não encontrado"}), 404
