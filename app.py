from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    return render_template("your_url.html", code=request.form['code'])