from flask import Flask
from mpbox import create_app

app = create_app()
#app = Flask(__name__)

from bliss import bp as bliss_bp
app.register_blueprint(bliss_bp)

from mp import bp as mp_bp
app.register_blueprint(mp_bp)

app.add_url_rule('/', endpoint='bliss.index')

if __name__ == "__main__":
    app.run()
