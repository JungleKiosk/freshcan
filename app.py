from flask import Flask, render_template
import data

app = Flask(__name__)

@app.route('/')
def home():
    animals = ['bear', 'duck', 'whale', 'mouse', 'cat', 'owl', 'cangaroo', 'delphine', 'gibbon']
    return render_template('home/home.html',data=data, animals=animals) # <h1>Hello Data ✅</h1>
    #return render_template('home/home.html') # <h1>NO DATA ❌</h1>


@app.route('/about')
def about():
    return render_template('home/about.html')
