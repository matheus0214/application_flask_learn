# Extensão do flask
def init_app(app):
    """Factory de inicialização de extensões"""

    @app.route("/")
    def index():
        return "<h1>Olá mundo!</h1>"

    @app.route("/contato")
    def contact():
        return "<form><input /></form>"
