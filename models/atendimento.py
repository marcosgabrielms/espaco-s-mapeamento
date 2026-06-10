from .db import db


class Atendimento(db.Model):
    __tablename__ = "atendimentos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("clientes.id"),
        nullable=False
    )

    problema = db.Column(
        db.Text,
        nullable=False
    )

    necessidade = db.Column(
        db.String(150),
        nullable=False
    )

    objetivo = db.Column(
        db.String(150),
        nullable=False
    )

    interesse = db.Column(
        db.String(20),
        nullable=False
    )

    prazo = db.Column(
        db.String(20),
        nullable=False
    )

    observacoes = db.Column(
        db.Text
    )

    classificacao = db.Column(
        db.String(50)
    )

    criado_em = db.Column(
        db.DateTime,
        server_default=db.func.now()
    )

    def __repr__(self):
        return f"<Atendimento {self.id}>"