# Neobis_final_project

## Custom registration and authorization by phone number project.
### Preparation and launch of the project
The first thing to do is to clone the repository:
***
```
$ git clone https://github.com/pavelchamgl/Neobis_final_project.git
$ cd authorization/
```
If poetry is not installed:
***
```
$ pip  install poetry
```
Install dependencies and activate the poetry virtual environment:
***
```
$ poetry shell
$ poetry install
```
Create an .env file with this params:
***
```
SECRET_KEY="enter your secret_key" 
DEBUG=True

TWILIO_ACCOUNT_SID = 'enter your twilio account sid'
TWILIO_AUTH_TOKEN = 'enter your twilio auth token'
TWILIO_PHONE_NUMBER = 'enter your twilio phone number'
```
Apply migrations:
***
```
python manage.py migrate
```
Run command for start server :
***
```
python manage.py runserver
```
The project is now up and running
***