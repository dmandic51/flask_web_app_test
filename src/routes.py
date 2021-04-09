from flask import flash
from flask import url_for
from flask import request
from flask import redirect
from flask import render_template

from src import db
from src import app
from src.database import Item
from src.database import User
from src.forms import RegisterForm
from src.forms import LoginForm
from src.forms import PurchaseItemForm
from src.forms import SellItemForm

from flask_login import login_user
from flask_login import current_user
from flask_login import logout_user
from flask_login import login_required


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    if request.method == 'POST':
        purchased_item = request.form.get('purchased_item')
        purchased_item = Item.query.filter_by(name=purchased_item).first()
        if purchased_item and current_user.can_purchase(purchased_item):
            purchased_item.buy(current_user)
            flash(f'Congratulations you purchased {purchased_item.name} for {purchased_item.price}$.',
                  category='success')
        elif purchased_item:
            flash(f'You don\'t have enough money to purchase {purchased_item.name} for {purchased_item.price}$.',
                  category='danger')
        return redirect(url_for('market_page'))

    if request.method == 'GET':
        items = Item.query.filter_by(owner=None)
        return render_template('market.html', items=items, purchase_form=purchase_form)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password_initial.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as: {user_to_create.username}', category='success')

        market_page_url = url_for('market_page')
        return redirect(market_page_url)

    if form.errors:
        for err_msg in form.errors.values():
            flash(err_msg, category='danger')

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Invalid username / password.', category='danger')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out.', category='info')
    return redirect(url_for('home_page'))
