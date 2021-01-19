from flask import Flask, jsonify
from threading import Thread
from cube import Cube
import random

app = Flask('')
cube = Cube()

@app.route('/code')
def code():
  return jsonify({
    "code": random.randint(100000, 999999)
  })

# Choo choo
def clean_string(str):
  return str.replace("%20", " ").replace("%27", "'").replace("’", "'").replace("‘","'").replace("\n","").replace("\t","").replace("%0D","").replace("%0A","")

@app.route('/<string:scr>/<string:sol>', methods=['GET'])
def home(scr, sol):
  scr = clean_string(scr)
  sol = clean_string(sol)
  return jsonify({
    "result": str(cube.check(scr, sol))
  })

def run():
	app.run(host='0.0.0.0',port=8080)

t = Thread(target=run)
t.start()