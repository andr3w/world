from flask import Flask, render_template
import json
w = json.load(open('worldl.json'))
app = Flask(__name__)

@app.route('/country/<num>')
def countryPage(num):
  return render_template('country.html',c = w[int(num)])

@app.route('/')
def indexPage(num):
  return render_template('index.html',continentList = set([c['continent'] for c in w]))

if __name__=='__main__':
  app.run(host='0.0.0.0',port=8080,debug=True)
