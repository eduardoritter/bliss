from flask import Blueprint, render_template
from constants import MP_DOMAIN


bp = Blueprint("mp", __name__, url_prefix="/", template_folder="templates")


@bp.route("/", methods=["GET", "POST"], host=MP_DOMAIN)
def index():
    return  render_template("mp.html")