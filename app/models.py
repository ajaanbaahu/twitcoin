from mongoengine import *

class Tweet(Document):
  text = StringField(required=True)
  classification = StringField(required=True)
  score = IntField(required=True)
  date=StringField(required=False)