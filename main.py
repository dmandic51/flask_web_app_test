#!/usr/bin/python3.9

from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False)

    def __repr__(self):
        return f'Item {self.name}'

@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


ITEMS = [
    {'name': 'Phone', 'barcode': '893212299897', 'price': 500, 'description': 'The best phone in the world.'},
    {'name': 'Laptop', 'barcode': '123985473165', 'price': 900, 'description': 'The best laptop in the world.'},
    {'name': 'Keyboard', 'barcode': '231985128446', 'price': 150, 'description': 'The best keyboard in the world.'},
    {'name': 'Mouse', 'barcode': '478522128446', 'price': 100, 'description': 'Not a pet.'},
    {'name': 'Dog', 'barcode': '233347868446', 'price': 200, 'description': 'A pet.'},
    {'name': 'Table', 'barcode': '968950128446', 'price': 50, 'description': 'DROP TABLES'},
]

def populate_db():
    db.create_all()
    for item in ITEMS:
        db_item = Item(**item)
        db.session.add(db_item)
    db.session.commit()


if __name__ == '__main__':
    populate_db()
    app.run(debug=True)
