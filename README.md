# Review-Me

## By Jared Ahaza, Michelle Claire and Immanuel Mugambi

# Description
[Review Me](https://github.com/Imma7/Review-Me.git) is a web application that enables a person to locate certain locations and check the description and reviews of the place of interest. 



## Features

##Specifications
[Specifications File](https://github.com/Imma7/Review-Me/blob/master/specs.md)

## Setup

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.

+ Python3.6

### Cloning the repository 
`git clone https://github.com/Imma7/Review-Me.git`

### Creating a virtual environment
`pip3 install virtualenv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Installing dependencies
`pip3 install -r requirements.txt`

### Running Tests
`python3.6 manage.py test`

### Running the Server
#### Development Mode
`The following configuration should be enabled when in development mode`


#### Production Mode
`The following configuration should be enabled when in production mode`


*Run Server*
Starting server by defaut will run it in development mode
`| python3.6 manage.py server |` or `| python3 manage.py server |` or `| python2 manage.py server|`

## Deployment to Heroku
Set the configuration in production mode 
` heroku create <app-name> `
` heroku heroku addons:create heroku-postgresql `
` git add . `
` git push heroku master `
` heroku run python3.6 manage.py db upgrade `


## Live Demo
[Review Me](https://reveiwme.herokuapp.com/)

## Technology Used
+ [Python](https://www.python.org)
+ [Flask](http://flask.pocoo.org/)
+ [Heroku](https://dashboard.heroku.com/apps)


## Contributions
[Immanuel Mugambi](https://github.com/Imma7) | [Michelle Claire](https://github.com/Monroe100) | [Jared Ahaza](https://github.com/JaredAhaza)

## License
MIT License (c) 2018 [Immanuel Mugambi](https://github.com/Imma7) 