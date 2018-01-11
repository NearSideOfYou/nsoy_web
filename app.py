__author__ = 'Cassie'


from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)
Bootstrap(app)
moment = Moment(app)


@app.route('/')
def home():
    return '<h1>Soon</h1>'


if __name__ == '__main__':
    app.run(debug=True)