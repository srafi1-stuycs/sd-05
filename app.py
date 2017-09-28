import csv
from util import occupation
from flask import Flask, render_template
app = Flask(__name__)

# renders a link to the occupations page
@app.route('/')
def index():
    return render_template('index.html')


# occupation.read_csv() returns a dictionary
@app.route('/occupations')
def occupations():
    return render_template('occupations.html',
            occupations = occupation.read_csv('data/occupations.csv'),
            rand_occupation = occupation.ret_rand() )

if __name__ == '__main__':
    app.run(debug=True)
