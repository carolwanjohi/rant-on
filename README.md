# Rant On
## This is a web application that allows users to log in using their Google accounts to go on and on about any topic., 11/12/2017


## By **[Carol Wanjohi](https://github.com/carolwanjohi)**

## Description
[This]() is a web application that prompts users to first log in using their Google credentials. After logging in the user is able to update their profile information, create a rant and react to other user's rants using emojis.

## User Stories
As a user I would like to:
* log in using Google
* set up a username and profile picture
* create a rant
* view other users rants
* react to other people's rants using emojis

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display log in | N/A | Display link for loggin in with Google |
| Create a user account | **Click** log in with Google button <br> Display Google log in form | Create a user account with a user profile and direct user to their profile |
| Update profile | **Click** update profile | Direct the user to a page with a form where the user can update their profile and submit the form |
| Create a rant | **Click** create icon  | Direct user to a page with a form where the user can create a rant and sumit the form |
| Display other user's rants | **Click** explore icon  | Direct user a page with a list of rants from other users |
| React to a rant with an emoji | **Click** an emoji | Hide he other emojis and only display the emoji selected  by the current user |

## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Virtual environment
* Postgres Database
* Internet


### Installation Process
1. Copy repolink
2. Run `git clone REPO-URL` in your terminal
3. Write `cd rant-on`
4. Create a virtual environment with `virtualenv virtual` or try `python3.6 -m venv virtual`
5. Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
```
6. Enter your virtual environment `source virtual/bin/activate`
7. Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
8. Create Postgres Database

```
psql
CREATE DATABASE rant
```
9. Change the database informatioin in `car/settings.py` 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rant',
        'USER': *POSTGRES_USERNAME*,
        'PASSWORD': *POSTGRES_USERNAME*,
    }
}
``` 
10. Run `./manage.py runserver` or `python3.6 manage.py runserver` to run the application

## Known Bugs
* no authentication system or log in
* update profile feature missing
* create rant feature missing
* seeing other user's rants missing
* react to other user's rants using emojis missing

## Technologies Used
- Python 3.6.2
- Django 1.11.7
- Bootstrap 3
- Postgres Database
- CSS
- HTML
- Heroku

### License

MIT (c) 2017 **[Carol Wanjohi](https://github.com/carolwanjohi)**





