###CRUD DB Operations
from project import db
from project.models.corsi import Corso, Tag
from project.models.serate import Serata
import datetime

#create models and tables
db.create_all()

tag1 = Tag("Falsk")
tag2 = Tag("Pygame")
tag3 = Tag("Sviluppo web")
tag4 = Tag("videogame")
tag5 = Tag("divertente")

db.session.add(tag1)
db.session.commit()
db.session.add(tag2)
db.session.commit()

corso_flask = Corso("Flask", "Andrea Guzzo", "Corso su sviluppo web con Flask", 6, "Facile")
corso_pygame = Corso("Pygame", "Mario Nardi", "Sviluppo videogame con pygame", 3, "Facile")

corso_flask.tags = [tag1, tag3]
corso_pygame.tags = [tag2, tag4, tag5]

db.session.add(corso_flask)
db.session.commit()
db.session.add(corso_pygame)
db.session.commit()

serata1 = Serata("Flask Serata 1", "Introduzione a flask", datetime.date(2020,10,12))
serata2 = Serata("Flask Serata 2", "Form con jinja", datetime.date(2020,10,19))
serata3 = Serata("Pygame", "Introduzione", datetime.date(2020,12,25))

db.session.add(serata1)
db.session.commit()
db.session.add(serata2)
db.session.commit()
db.session.add(serata3)
db.session.commit()

#recupera gli id di un corso
flask = Corso.query.filter_by(nome="Flask").first()
pygame = Corso.query.filter_by(nome="Pygame").first()

serata1.corso_id = flask.id
serata2.corso_id = flask.id
serata3.corso_id = pygame.id

###PRIMA DI CONTINUARE CONTROLLARE
###CHECK
course = Corso.query.all()
print("List of courses: ", course)