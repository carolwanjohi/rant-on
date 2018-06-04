# Rant On

#### By **[Carol Wanjohi](https://github.com/carolwanjohi)**

## Description
[This](https://rant-on.herokuapp.com/) is a web application that prompts users to first log in using their Google credentials. After logging in the user is able to update their profile information, create a rant and react to other user's rants using emojis.

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
| Display log in | N/A | Display button for user to log in with Google |
| Create a user account | **Click** log in with Google button <br> Display Google log in form | Create a user account with a user profile and direct user to their profile |
| Update profile | **Click** update profile | Direct the user to a page with a form where the user can update their profile and submit the form |
| Create a rant | **Click** create rant  | Direct user to a page with a form where the user can create a rant and sumit the form |
| Display other user's rants | **Click** home icon or site icon | Direct user a page with a list of rants from other users |
| React to a rant with an emoji | **Click** an emoji | Hide he other emojis and only display the emoji selected  by the current user |

## Setup/Installation Requirements

### Prerequisites
* Python 3.6.2
* Virtual environment
* Postgres Database
* Internet


### Installation Process
```
git clone https://github.com/carolwanjohi/rant-on.git && cd cd rant-on
virtualenv virtual or python3.6 -m venv virtual
source virtual/bin/activate
pip3 install -r requirements.txt
```
* Create .env file `touch .env` and add the following:
```
SECRET_KEY=<your secret key>
DEBUG=True
USER=<your postgresql username>
PASSWORD=<your postgresql password>
```
* Create Postgres Database
```
psql
CREATE DATABASE rant;
```
### Running the application
```
./manage.py runserver or python3.6 manage.py runserver
```

### Running the tests
```
./manage.py test or python3.6 manage.py test
```

## Known Bugs

No known bugs

## Technologies Used
- Python 3.6.2
- Django 1.11.7
- Google Plus API
- Bootstrap 3
- Postgres Database
- CSS
- HTML
- Heroku

### License

MIT (c) 2017 **[Carol Wanjohi](https://github.com/carolwanjohi)**





