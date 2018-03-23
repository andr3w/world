#For this to be deployed you must
#Use the file name server.py
#Use the variable name app
#This is because server:app has been hard coded in /etc/uwsgi-emperor/vassals/40000036.ini
from flask import Flask
app = Flask(__name__)

@app.route('/')
def indexPage():
  return "{}".format(6*7)

if __name__=='__main__':
  app.run(host='0.0.0.0',port=5036,debug=True)
