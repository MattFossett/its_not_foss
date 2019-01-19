# its_not_foss
Web app for sharing dumb stuff in 141 cottage d 

TODO: Look into pip freeze instead of needing venv on git
 WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.

Here are the packages used:

python3
virtual enviornment venv:
    $ python3 -m venv venv
To activate the virtual enviornment:
    $ source venv/bin/activate
NOTE: The following assume that you are in an activated virtual enviornment
flask: 
    pip install flask
Dotenv for configuring enviornment variables:
    pip install python-dotenv
wtforms is an extension for form processing:
    pip install flask-wtf
sqlalchemy: for interacting with database:
    pip install flask-sqlalchemy
bcrypt: for hashing new passwords:
    pip install flask-bcrypt
flask-login: 
    pip install flask-login
pillow: for picture processing
    pip install pillow
waitress: production server:
    pip install waitress


OUR PURPOSES:
1. Activate venv:
        source venv/bin/activate
2. Configure desired settings in run.py
3. Start flask server:
        python3 run.py

PUT UP PRODUCTION SERVER:

1. Activate venv:
        source venv/bin/activate
2. Start up server with waitress:
        waitress-serve --call 'not_foss:create_app'
