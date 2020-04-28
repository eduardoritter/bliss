from flask import Blueprint, render_template


bp = Blueprint('bliss', __name__, url_prefix='/bliss', template_folder='templates', static_folder='static')


@bp.route('/', methods=['GET', 'POST'])
def index():
    return  render_template('bliss.html')
