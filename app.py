from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/home.html', data=data)


