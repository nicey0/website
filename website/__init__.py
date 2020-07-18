import os
from flask import Flask


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev",
    DATABASE=os.path.join(app.instance_path, 'website.sqlite')
)

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
