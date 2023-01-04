from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "I am immortal"

def run():
  app.run(host='0.0.0.0', port = 8080)

def jinda():
  t=Thread(target = run)
  t.start()
