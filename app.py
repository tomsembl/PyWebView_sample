from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=["GET"])
def homepage():
    return render_template('home.html')

app.run()