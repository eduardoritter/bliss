from flask import Blueprint, render_template
from constants import BLISS_DOMAIN


bp = Blueprint("bliss", __name__, url_prefix="/", template_folder="templates")


@bp.route("/", methods=["GET", "POST"], host=BLISS_DOMAIN)
def index():
    return  render_template("bliss.html")
