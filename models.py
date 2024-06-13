from . import app, db
from flask_sqlalchemy import SQLAlchemy

class vue_cours_ressources(db.Model):
    cours_id = db.Column(db.Integer,primary_key=True)
    titre= db.Column(db.String(100),nullable=False)
    description= db.Column(db.String(200),nullable=False)
    ressource_id = db.Column(db.Integer,primary_key=True)
    type= db.Column(db.String(100),nullable=False)
    url= db.Column(db.String(200),nullable=False)

    def __repr__(self):
        return f'{self.cours_id} : {self.titre} : {self.description} : {self.ressource_id} : {self.type} : {self.url}'
