from mongoengine import *
import pymongo
from pymongo import Connection



class generate_series(Document):
	Day=StringField(required=True)
	hour=StringField(required=True)
	counts=StringField(required=False)
	negative=StringField(required=False)
	neutral=StringField(required=False)
	bot=StringField(required=False)
	#meta={"db_alias":"default"}
	
	


