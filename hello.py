from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello flask!"


@app.route('/about')
def about():
    return "This is a url shortener"