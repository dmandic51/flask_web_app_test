
from flask import flash
from flask import url_for
from flask import redirect
from flask import render_template

from src import db
from src import app
from src.database import Item
from src.database import User
from src.forms import RegisterForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    registration_form = RegisterForm()
    if registration_form.validate_on_submit():
        user_to_create = User(username=registration_form.username.data,
                              email_address=registration_form.email_address.data,
                              password_hash=registration_form.password_initial.data)
        db.session.add(user_to_create)
        db.session.commit()

        market_page_url = url_for('market_page')
        return redirect(market_page_url)

    if registration_form.errors:
        for err_msg in registration_form.errors.values():
            flash(err_msg, category='danger')

    return render_template('register.html', form=registration_form)
