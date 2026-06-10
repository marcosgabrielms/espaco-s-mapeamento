from .db import db


class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False
    )

    telefone = db.Column(
        db.String(20),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        nullable=False
    )

    como_conheceu = db.Column(
        db.String(50)
    )

    criado_em = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    atendimentos = db.relationship(
        "Atendimento",
        backref="cliente",
        lazy=True
    )

    def __repr__(self):
        return f"<Cliente {self.nome}>"