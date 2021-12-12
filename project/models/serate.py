from project import db

class Serata(db.Model):

    __tablename__ = "serata"

    __table_args__ = (db.UniqueConstraint("id", "data", name="constraint_serata"),) #vincolo id, orario serata

    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descrizione = db.Column(db.String(255), nullable=False)
    data = db.Column(db.DateTime())
    corso_id = db.Column(db.Integer(), db.ForeignKey("corso.id"))

    def __init__(self, nome, descrizione, data):
        self.nome = nome
        self.descrizione = descrizione
        self.data = data

    def __repr__(self):
        return ("\nSerata: {self.nome}, descrizione: {self.descrizione} in data {self.data}")