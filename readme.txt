TODO: Look into pip freeze instead of needing venv on git

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
