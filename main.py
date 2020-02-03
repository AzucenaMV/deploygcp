from flask import Flask, render_template,redirect,flash,request,url_for
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
table = pd.read_csv("https://raw.githubusercontent.com/AzucenaMV/CapstoneProject/master/data/sp500/SP500table.csv")
df = pd.read_csv("https://raw.githubusercontent.com/AzucenaMV/CapstoneProject/master/data/sp500/stock_prices_sub.csv")

@app.route('/',methods=['GET', 'POST'])
def index2():
    stock = request.form.get('comp_select')
    if stock == None:
        stock='AAL'
    name = table[table['Symbol'] == stock].Security.values[0]
    df['Date'] = pd.to_datetime(df['Date'],infer_datetime_format=True)
    plt.figure(figsize=(40,20))
    plt.title('Stock Price: {}'.format(stock), fontsize=60)
    plt.plot(df['Date'],df[stock], color = '#a2b969')
    plt.ylabel('Price (USD)', fontsize=40)
    plt.xlabel('Date', fontsize=40)
    plt.savefig('/tmp/square_plot.png')
    ### Saving plot to disk in png format
    #plt.savefig('static/images/square_plot.png')
    ### Rendering Plot in Html
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    plt.close()
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = figdata_png
    return render_template(
        'index2.html',
        data=list(df)[3::],result=result,stock=stock, name = name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)