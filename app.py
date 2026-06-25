from flask import Flask
app = Flask(__name__)

@app.route('/try/<int:id>/')
def try_again(id):
  return "Работай фиговина ты поганая #{}".format(id)

@app.route('/')
def hello_world():
  return "Работай фиговина ты поганая "


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)