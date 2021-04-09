#!/usr/bin/python3.9

from src import app
from src.database import populate_db

ITEMS = [
    {'name': 'Phone', 'barcode': '893212299897', 'price': 500, 'description': 'The best phone in the world.'},
    {'name': 'Laptop', 'barcode': '123985473165', 'price': 900, 'description': 'The best laptop in the world.'},
    {'name': 'Keyboard', 'barcode': '731985128446', 'price': 150, 'description': 'The best keyboard in the world.'},
    {'name': 'Mouse', 'barcode': '478522128446', 'price': 100, 'description': 'Not a pet.'},
    {'name': 'Dog', 'barcode': '233347868446', 'price': 200, 'description': 'A pet.'},
    {'name': 'Table', 'barcode': '968950128446', 'price': 50, 'description': 'DROP TABLES'},
]
USERS = [
    {'username': 'aaa', 'email_address': 'aaa@aaa.aa', 'password': 'aaaaaa'}
]
if __name__ == '__main__':
    populate_db(ITEMS, USERS)
    app.run(debug=True)
