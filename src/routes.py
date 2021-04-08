
from flask import render_template

from src import app
from src.database import Item
from src.forms import RegisterForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register')
def register_page():
    registration_form = RegisterForm()
    if registration_form.validate_on_submit():
        pass
    return render_template('register.html', form=registration_form)
