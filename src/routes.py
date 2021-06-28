from flask import Blueprint, render_template

bp = Blueprint('routes', __name__)


@bp.route("/")
def index():
    """ Index page """
    return render_template("index.html")