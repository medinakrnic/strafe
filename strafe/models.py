from flask_sqlalchemy import SQLAlchemy
from strafe import app

db = SQLAlchemy(app)

class Team(db.Model):
    
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String, unique = True, nullable = False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
        
    def __init__(self, name):
        self.name = name

    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }


class Match(db.Model):

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String, unique = True, nullable = False)
    home_team = db.Column(db.ForeignKey(Team.id), nullable = False)
    guest_team = db.Column(db.ForeignKey(Team.id), nullable = False)
    home_score = db.Column(db.Integer, default = 0)
    guest_score = db.Column(db.Integer, default = 0)
    date_time = db.Column(db.DateTime)

    def __init__(self, name, home_team, guest_team, date_time):
        self.name = name
        self.home_team = home_team
        self.guest_team = guest_team
        self.date_time = date_time

    def __str__(self):

        return self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'home_team': self.home_team,
            'guest_team': self.guest_team,
            'home_score': self.home_score,
            'guest_score': self.guest_score,
            'date_time': self.date_time
        }



db.create_all()
