from flask import Flask, render_template
from ppp import get_data
import pygal
currSymbols =[]
app = Flask('app')
@app.route('/')
def hello_world():
  data = get_data()

  #Currencies for each country, hard coded country codes. work later on this. 
  symbol1 = data[0]['currencies']['CAD']['symbol']
  symbol2 = data[3]['currencies']['INR']['symbol']
  symbol3 = data[6]['currencies']['UAH']['symbol']
  symbol4 = data[9]['currencies']['TRY']['symbol']

  currSymbols.append(symbol1)
  currSymbols.append(symbol2)
  currSymbols.append(symbol3)
  currSymbols.append(symbol4)
  
  
  bar_chart = pygal.Bar()
  bar_chart.title = 'Purchasing Power of various countries'
  bar_chart.add(data[0]['country_name'], data[0]['dollar_ppp'])
  bar_chart.add(data[3]['country_name'], data[3]['dollar_ppp'])
  bar_chart.add(data[6]['country_name'], data[6]['dollar_ppp'])
  bar_chart.add(data[9]['country_name'], data[9]['dollar_ppp'])
  bar_chart.render_to_file('static/images/ppp_chart.svg') 
  
  return render_template("index.html",data=data, currSymbols = currSymbols)

app.run(host='0.0.0.0', port=8080)
