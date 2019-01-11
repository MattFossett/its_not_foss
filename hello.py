from flask import Flask
from flask import render_template
#from flask import routes
from flask import url_for


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html', title='Hello!')


