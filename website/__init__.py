import os
from flask import Flask

app = Flask(__name__)

class Production:
    SECRET_KEY = os.urandom(32)
    DATABASE = os.path.join(app.instance_path, 'website.sqlite')
class Development:
    SECRET_KEY = "dev"
    DATABASE = os.path.join(app.instance_path, 'dev.sqlite')
app.config.from_object(Production())

try:
    os.makedirs(app.instance_path)
except OSError:
    pass

# Database
from . import db
db.init_app(app)

# Main
from . import main
app.register_blueprint(main.bp)
app.add_url_rule("/", endpoint="index")

# Auth
from . import auth
app.register_blueprint(auth.bp)
