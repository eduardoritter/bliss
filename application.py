from flask import Flask, Blueprint, request
from constants import BLISS_DOMAIN

#from mpbox import create_app

#app = create_app()
app = Flask(__name__, host_matching=True, static_host=BLISS_DOMAIN)

from bliss import bp as bliss_bp
app.register_blueprint(bliss_bp)

from mp import bp as mp_bp
app.register_blueprint(mp_bp)

if __name__ == "__main__":
    app.debug = True
    app.run()
