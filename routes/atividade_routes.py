from flask import Blueprint, request, jsonify
from services import atividade_service

atividade_bp = Blueprint("atividades", __name__, url_prefix="/atividades")

@atividade_bp.route("/", methods=["GET"])
def get_all():
    return jsonify(atividade_service.listar_atividades())

@atividade_bp.route("/<int:id>", methods=["GET"])
def get_by_id(id):
    a = atividade_service.obter_atividade(id)
    if a:
        return jsonify(a)
    return jsonify({"erro": "Atividade não encontrada"}), 404

@atividade_bp.route("/", methods=["POST"])
def create():
    dados = request.json
    return jsonify(atividade_service.criar_atividade(dados)), 201

@atividade_bp.route("/<int:id>", methods=["PUT"])
def update(id):
    dados = request.json
    atualizada = atividade_service.atualizar_atividade(id, dados)
    if atualizada:
        return jsonify(atualizada)
    return jsonify({"erro": "Atividade não encontrada"}), 404

@atividade_bp.route("/<int:id>", methods=["DELETE"])
def delete(id):
    atividade_service.deletar_atividade(id)
    return "", 204