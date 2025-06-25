def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return {"erro": "Recurso não encontrado"}, 404

    @app.errorhandler(400)
    def bad_request(error):
        return {"erro": "Requisição inválida"}, 400

    @app.errorhandler(500)
    def server_error(error):
        return {"erro": "Erro interno do servidor"}, 500
