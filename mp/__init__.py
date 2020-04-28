from flask import Blueprint, render_template


bp = Blueprint('mp', __name__, url_prefix='/mp', template_folder='templates', static_folder='static')


@bp.route('/', methods=['GET', 'POST'])
def index():
    return  render_template('mp.html')