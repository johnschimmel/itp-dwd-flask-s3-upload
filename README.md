## Flask uploading file to s3 with Boto

## Skip to Step 5 if you have an existing app from class and you want to add file upload support.

### Our requirements.txt

	Flask==0.10
	Flask-mongoengine==0.7.0
	boto==2.17.0

## Changes to App.py & Models.py

### We're only requiring Flask-mongoengine

Since we started with Databases and Form validation we have been including both mongoengine and flask-mongoengine. This was bad form on my part.  

Mongoengine and Flask-mongoengine do the same thing but Flask-mongoengine is a little better for our needs.

### app.py updates

Top of the file currently, we imported mongoengine

	# import all of mongoengine
	from mongoengine import *

Change this to...

	# import all of mongoengine
	from flask.ext.mongoengine import mongoengine


We connected to the database a few lines from the top with

	# --------- Database Connection ---------
	# MongoDB connection to MongoLab's database
	connect('mydata', host=os.environ.get('MONGOLAB_URI'))

Change this to...

	mongoengine.connect('mydata', host=os.environ.get('MONGOLAB_URI'))


### models.py updates

The import and from/import statements at the top of **models.py** is currently

	from mongoengine import *
	from flask.ext.mongoengine.wtf import model_form
	from datetime import datetime

Change to this...

	from flask.ext.mongoengine.wtf import model_form
	from wtforms.fields import * # for our custom signup form
	from flask.ext.mongoengine.wtf.orm import validators
	from flask.ext.mongoengine import *
	from datetime import datetime

We are updating the imports to use more field validation techniques.

Our models change a bit too. Previously we defined Models as such, 

	class Blogpost(Document):
		title = StringField(max_length=120, required=True, verbose_name="First name")
		description = StringField(required=True)
		...

We now define models like so, 

	class Blogpost(mongoengine.Document):
		title = mongoengine.StringField(max_length=120, required=True)
		description = mongoengine.StringField()
		...

We create forms like this

	photo_form = model_form(Image)


But we can also use WTForms directly like this,

	# Create a WTForm form for the photo upload.
	# This form will inhirit the Photo model above
	# It will have all the fields of the Photo model
	# We are adding in a separate field for the file upload called 'fileupload'

	class photo_upload_form(photo_form):
		fileupload = FileField('Upload an image file', validators=[])

**photo_upload_form** can be used like any other form we use before. Using WTForm directly gives us a few more options than we previously had. We will use this again in the User management app demo.



## Getting Started 

### Step 1 : Download code, setup Git, heroku create

1. Download the sample code from [Github](https://github.com/johnschimmel/itp-dwd-flask-s3-upload)
2. Navigate to code directory in Terminal. Create Git repo

		git init
		git add .
		git commit -m "initial commit"

	Create virtual environment and install requirements

		virtualenv venv
		. runpip

3. Create a new Heroku app

		heroku create


### Step 2 : Adding MongoLabs to your Heroku App

Heroku offers a [lot of different Add-ons](https://addons.heroku.com/) for your apps. Many different types of databases, image tools, cache utilities are available from 3rd party companies. Many offer a trial plan to test and develop with before you commit to a paid plan.

MongoLabs offers a [250MB MongoDB instance for free](https://addons.heroku.com/mongolab) (see here) : ) How wonderful.

To install the MongoLabs 

* Navigate to the code folder of your app
* In Terminal, add the MongoLab starter plan

		heroku addons:add mongolab:starter

This has added MongoLab to your app.

### Step 3: Configure your local environment

When adding Add-ons, Heroku will add the required configuration variables for the services including username, password, urls, etc. 

We must create a local configuration file to allow our local development server to connect to the MongoLabs MongoDB instance. We can grab a copy of our Heroku configuration variables and put them inside a **.env** file, our environment variable file.

Run the following command inside your code folder.

	heroku config --shell | grep MONGOLAB_URI >> .env

This will create a new file, **.env**  and it will contain a single line starting with MONGOLAB_URI and followed by a long connection url. This is the username and password for your MongoLabs account.

.env

	MONGOLAB_URI=mongodb://heroku_app8083291:sadlfkwewe........

### Step 4: Add .env to .gitignore file

We want GIT to ignore the .env file, **VERY IMPORTANT**  This keeps our environment variables safe and they won't get included inside our GIT repository (or worse, get pushed to Github).

Open your .gitignore file and add '.env' on a new line. Save the file.

.gitignore

	.env
	venv
	*.pyc
	

### Step 5: Register with Amazon Web Services

Create an account on Amazon Web Services, you can use your Amazon account, [http://aws.amazon.com/console/](http://aws.amazon.com/console/) Click on the Sign Up button.

### Step 6: Log in and create new S3 bucket

When you're registered and logged into the AWS site, visit the console, [https://console.aws.amazon.com/console/home?#](https://console.aws.amazon.com/console/home?#)

In the Storage and Content Delivery section click on S3, scalable storage in the cloud, [https://console.aws.amazon.com/s3/home](https://console.aws.amazon.com/s3/home).

Now we will create a bucket (like a directory). The bucket will be the container for your uploaded files. On the left panel of the S3 console, click 'Create Bucket'. Provide a **bucket name** and leave the **Region** to US Standard. Then click **Create**.

### Step 7: Add environment variables to .env and Heroku

Inside the AWS Console, on the top menu bar click on your name, then click **SECURITY CREDENTIALS**.

On the SECURITY CREDENTIALS page, you will have access to

* ACCESS KEY ID
* SECRET ACCESS KEY

Open your .env file and add 3 new variables for Amazon AWS

**.env**

	AWS_BUCKET=YOURBUCKNAME
	AWS_ACCESS_KEY_ID=XXXXXXXXXXXX
	AWS_SECRET_ACCESS_KEY=XXXXXXXXXXX
	SECRET_KEY=SOMETHINGSECRETFORFLASK

Save your .env file.

Now let's push the new AWS variable to Heroku config, run the commands in Terminal

	heroku config:add SECRET_KEY=SOMETHINGSECRETFORFLASK
	heroku config:add AWS_BUCKET=YOURBUCKNAME
	heroku config:add AWS_ACCESS_KEY_ID=XXXXXXXXXXXX
	heroku config:add AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXX


You can confirm the AWS variables are on heroku by running the command,

	heroku config


### Start your servers

	. start

or

	foreman start

