# -*- coding: utf-8 -*-
from flask.ext.mongoengine.wtf import model_form
from wtforms.fields import * # for our custom signup form
from flask.ext.mongoengine.wtf.orm import validators
from flask.ext.mongoengine import *
from datetime import datetime

class Comment(mongoengine.EmbeddedDocument):
	name = mongoengine.StringField()
	comment = mongoengine.StringField()
	timestamp = mongoengine.DateTimeField(default=datetime.now())

class Photo(mongoengine.Document):

	title = mongoengine.StringField(max_length=120, required=True)
	creator = mongoengine.StringField(max_length=120, required=True, verbose_name="Photographer name")
	
	tags = mongoengine.ListField( mongoengine.StringField())

	filename = mongoengine.StringField()

	# Comments is a list of Document type 'Comments' defined above
	comments = mongoengine.ListField( mongoengine.EmbeddedDocumentField(Comment) )

	# Timestamp will record the date and time idea was created.
	timestamp = mongoengine.DateTimeField(default=datetime.now())


# Create a Validation Form from the Idea model
PhotoForm = model_form(Photo)

	

