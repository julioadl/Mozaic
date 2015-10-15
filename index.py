from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/<date>')
def get_data_from_date(date):
    return render_template('exploreResults.html', menu=date)

if __name__ == '__main__':
    app.run(debug = True)
