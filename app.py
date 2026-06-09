from flask import Flask, render_template, request, redirect, url_for

from config import Config
from models.models import db, Cliente

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cliente/novo")
def novo_cliente():
    return render_template("cliente_form.html")

@app.route("/cliente/salvar", methods=["POST"])
def salvar_cliente():

    cliente = Cliente(
        nome = request.form["nome"],
        telefone = request.form["telefone"],
        email = request.form["email"],
        empresa = request.form["empresa"],
        tipo = request.form["tipo"],
        origem = request.form["origem"]
    )

    db.session.add(cliente)
    db.session.commit()

    return redirect(url_for("listar_clientes"))

@app.route("/clientes")
def listar_clientes():
    
    clientes = Cliente.query.all()

    return render_template(
        "clientes.html",
        clientes=clientes
    )

if __name__ == "__main__":
    app.run(debug=True)