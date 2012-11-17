# -*- coding: utf-8 -*-
import os, datetime, re
from flask import Flask, request, render_template, redirect, abort

# import all of mongoengine
from flask.ext.mongoengine import mongoengine

# import data models
import models

app = Flask(__name__)   # create our flask app
app.config['secret_key'] = os.environ.get('SECRET_KEY')
app.config['CSRF_ENABLED'] = True

# --------- Database Connection ---------
# MongoDB connection to MongoLab's database
mongoengine.connect('mydata', host=os.environ.get('MONGOLAB_URI'))
app.logger.debug("Connecting to MongoLabs")

# --------- Routes ----------

# this is our main page
@app.route("/", methods=['GET','POST'])
def index():

	# get Idea form from models.py
	photo_form = models.PhotoForm(request.form)
	
	# if form was submitted and it is valid...
	if request.method == "POST" and photo_form.validate():
	
		# get form data - create new idea
		# idea = models.Idea()
		# idea.creator = request.form.get('creator','anonymous')
		# idea.title = request.form.get('title','no title')
		# idea.slug = slugify(idea.title + " " + idea.creator)
		# idea.idea = request.form.get('idea','')
		# idea.categories = request.form.getlist('categories') # getlist will pull multiple items 'categories' into a list
		
		# idea.save() # save it

		# redirect to the new idea page
		return redirect('/ideas/%s' % idea.slug)

	else:

		
		# render the template
		templateData = {
			
			'form' : photo_form
		}

		return render_template("main.html", **templateData)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404



# --------- Server On ----------
# start the webserver
if __name__ == "__main__":
	app.debug = True
	
	port = int(os.environ.get('PORT', 5000)) # locally PORT 5000, Heroku will assign its own port
	app.run(host='0.0.0.0', port=port)



	