from flask import Flask, render_template
from flask import jsonify
import pandas as pd
import wikipedia

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)