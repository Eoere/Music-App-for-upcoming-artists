from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Comment (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    music_id = db.Column(db.Integer, db.ForeignKey('music.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('comments', lazy=True))
    music = db.relationship('Music', backref=db.backref('comments', lazy=True))
class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    music_file = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('musics', lazy=True))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    firstName=db.Column(db.String(150))
