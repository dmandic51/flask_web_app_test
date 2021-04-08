
from flask import Flask


app = Flask(__name__)


@app.route('/')
def print_hi():
    return 'hello there'


if __name__ == '__main__':
    app.run(debug=True)
