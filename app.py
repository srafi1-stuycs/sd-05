import csv, occupation
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/occupations')
def occupations():
    return render_template('occupations.html',
            occupations = occupation.read_csv(),
            rand_occupation = occupation.ret_rand() )

if __name__ == '__main__':
    app.run(debug=True)
