from flask import Flask, render_template
from routes.dashboard_routes import dashboard_bp
from config import Config
from models import db

from routes.cliente_routes import (
    cliente_bp
)

from routes.atendimento_routes import (
    atendimento_bp
)

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(
    cliente_bp
)

app.register_blueprint(
    atendimento_bp
)
app.register_blueprint(
    dashboard_bp
)

@app.route("/")
def index():

    from flask import render_template

    return render_template(
        "home/index.html"
    )


if __name__ == "__main__":
    app.run(debug=True)