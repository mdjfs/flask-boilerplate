import os
from . import routes
from .server import Server
from flask.cli import AppGroup, with_appcontext
from flask import current_app

doc_cli = AppGroup("documentation", help="Documentation generation")

@doc_cli.command("generate", help="Generate docs")
@with_appcontext
def create_doc():
    os.system("sphinx-apidoc -o docs/source/ src/ -f")
    os.system("sphinx-build -b html docs/source/ docs/build/")


def create_app():
    """ Creates flask app instance """
    app = Server(instance_relative_config=True)
    app.config.from_mapping(
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )
    app.config.from_pyfile('config.py', silent=True)
    app.register_blueprint(routes.bp)
    app.cli.add_command(doc_cli)

    # You can init app for any modules, example, database.init_app(app)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
