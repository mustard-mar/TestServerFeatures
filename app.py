from flask import Flask
name = 'main'
app = Flask(name)

@app.route('/')
def hello_world():
  return 'Работай фиговина ты поганая'

if name == 'main':
  app.run(debug=True)