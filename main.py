#!/usr/bin/python3.9

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/market')
def market():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150},
        {'id': 4, 'name': 'Mouse', 'barcode': '478522128446', 'price': 100},
        {'id': 5, 'name': 'Dog', 'barcode': '233347868446', 'price': 200},
        {'id': 6, 'name': 'Table', 'barcode': '968950128446', 'price': 50},
    ]
    return render_template('market.html', items=items)


if __name__ == '__main__':
    app.run(debug=True)
