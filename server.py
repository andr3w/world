from flask import Flask, render_template
import json
w = json.load(open('worldl.json'))
app = Flask(__name__)

@app.route('/country/<num>')
def countryPage(num):
  return render_template('country.html',c = w[int(num)])

@app.route('/countryByName/<name>')
def countryByNamePage(name):
  return render_template('country.html',
          c = next(c for c in w if c['name'] == name)
          )

@app.route('/continent/<name>')
def continentPage(name):
  return render_template('continent.html',
          continentName = name,
          countryList = [c for c in w if c['continent']==name]
          )

@app.route('/')
def indexPage():
  return render_template('index.html',continentList = set([c['continent'] for c in w]))

if __name__=='__main__':
  app.run(host='0.0.0.0',port=8080,debug=True)
