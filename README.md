## MongoDB library - Mongoengine

[Mongoengine](http://mongoengine.org/)

Adding Mongoengine to requirements.txt

	Mongoengine==0.7.5
	unidecode


## Getting Started with MongoDB on Heroku

We will be using MongoLabs as our MongoDB host service, they have a free starter plan that we can easily associate with our Heroku accounts. When we have added the MongoLabs service we will have a connection string that includes username, password and URI to the database server.

### Step 1 : Download code, setup Git, heroku create

1. Download the sample code from [Github](https://github.com/johnschimmel/ITP-DWD-Fall-2012-Week-5)
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

	heroku config --shell > .env

This will create a new file, **.env**  and it will contain a single line starting with MONGOLAB_URI and followed by a long connection url. This is the username and password for your MongoLabs account.

.env

	MONGOLAB_URI=mongodb://heroku_app8083291:sadlfkweweroi........

### Step 4: Add .env to .gitignore file

We want GIT to ignore the .env file, **VERY IMPORTANT**  This keeps our environment variables safe and they won't get included inside our GIT repository (or worse, get pushed to Github).

Open your .gitignore file and add '.env' on a new line. Save the file.

.gitignore

	.env


### Step 5: Start your servers

	. start

or

	foreman start
