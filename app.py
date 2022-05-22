from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/index')
def home():
    return render_template('index.html')
    # return index()

@app.route('/movie')
def movie():
    con=sqlite3.connect("movie.db")
    cur=con.cursor()
    sql="select * from"
    return render_template('movie.html')

@app.route('/score')
def score():
    return render_template('score.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/word')
def word():
    return render_template('word.html')

if __name__ == '__main__':
    app.run()
