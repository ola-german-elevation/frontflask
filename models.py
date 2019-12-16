from flask_mongoengine import MongoEngine
import mongoengine as me

db = MongoEngine()


class Rasp(db.Document):
    serial = db.StringField(required=True, max_length=60)
    wlan = db.StringField()
    connected = db.BooleanField(default=False)
    # last_conected = db.DateTime()


class Member(db.Document):
    name = db.StringField(max_length=60)
    email = db.StringField(max_length=100)


class Team(db.Document):
    id = db.StringField(required=True, max_length=60)
    members = db.ListField(Member)
    # rasp = db.Document(Rasp)

