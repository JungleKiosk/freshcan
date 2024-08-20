from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import data

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psqcopg2://postgres:password@localhost:5432/fc_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Favitems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    items = db.Column(db.String(2000))



@app.route('/')
def home():
    animals = ['bear', 'duck', 'whale', 'mouse', 'cat', 'owl', 'cangaroo', 'delphine', 'gibbon']
    return render_template('home/home.html',data=data, animals=animals) # <h1>Hello Data ✅</h1>
    #return render_template('home/home.html') # <h1>NO DATA ❌</h1>


@app.route('/about')
def about():
    return render_template('home/about.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)