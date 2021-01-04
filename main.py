from flask import Flask, jsonify
from threading import Thread
from cube import Cube

app = Flask('')
cube = Cube()

@app.route('/<string:scr>/<string:sol>', methods=['GET'])
def home(scr, sol):
  scr = scr.replace("%20", " ").replace("%27", "'").replace("’", "'")
  sol = sol.replace("%20", " ").replace("%27", "'").replace("’", "'")
  return jsonify({
    "result": str(cube.check(scr, sol))
  })

def run():
	app.run(host='0.0.0.0',port=8080)

t = Thread(target=run)
t.start()
