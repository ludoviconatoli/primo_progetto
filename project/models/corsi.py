from project import db

#creazione schema tabelle - relazione N a N
tags = db.Table(
    "corso_tags",
    db.Column("corso_id", db.Integer, db.ForeignKey("corso.id", primary_key=True)),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id", primary_key=True))
)

class Corso(db.Model): #sottoclasse di un modello

    __tablename__ = "corso"

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    insegnante = db.Column(db.String(100))
    descrizione = db.Column(db.String(255))
    lezioni = db.Column(db.Integer())
    livello = db.Column(db.String(100))

    # creazione relazione 1 corso N serate
    serate = db.relationship(
        "Serata", backref="corso", lazy="subquery"
    )

    tags = db.relationship("Tag", backref="corso", lazy=True, secondary=tags)

    def __init__(self, nome, insegnante, descrizione, lezioni, livello):
        self.nome = nome
        self.insegnante = insegnante
        self.descrizione = descrizione
        self.lezioni = lezioni
        self.livello = livello

    def __repr__(self):
        return '\nCorso: {self.nome}, tenuto da: {self.insegnante}, livello:{self.livello} '

class Tag(db.Model):
    __tablename__ = "tag"

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Tag: {self.name} with id: {self.id}"
