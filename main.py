from flask import Flask, render_template
from flask import jsonify
import pandas as pd
import numpy as np
import wikipedia
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)


@app.route('/<stock>')
def index(stock):
    df = pd.read_csv("https://raw.githubusercontent.com/AzucenaMV/CapstoneProject/master/data/sp500/stock_prices.csv")
    ### Generating The Plot
    df['Date'] = pd.to_datetime(df['Date'],infer_datetime_format=True)
    plt.plot(df['Date'],df[stock])
    ### Saving plot to disk in png format
    plt.savefig('static/images/square_plot.png')
    #plt.savefig('/tmp/square_plot.png')

    ### Rendering Plot in Html
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    plt.close()
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = figdata_png
    return render_template('index.html', result=result)

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