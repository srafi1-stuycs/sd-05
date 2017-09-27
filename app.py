import csv, occupation
from flask import Flask, render_template
app = Flask(__name__)


def read_csv():
    with open('data/occupations.csv', 'rU') as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        occupations = []
        for row in reader:
            occupations.append(row)
        return occupations

@app.route('/')
def index():
    return render_template('index.html')

occupation.read_csv()

@app.route('/occupations')
def occupations():
    return render_template('occupations.html',
            occupations = read_csv(),
            rand_occupation = occupation.ret_rand() )

if __name__ == '__main__':
    app.run(debug=True)
