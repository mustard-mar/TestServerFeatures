from flask import Flask, render_template

app = Flask(__name__)


@app.route('/try/<int:id>/')
def try_again(id):
  return "Работай фиговина ты поганая #{}".format(id)

@app.route('/user/<username>')
def user_info(username):
  user_data = {'username': "yakuba", 'email': 'yakuba@example.com', 'is_active': True}
  return render_template('base.html',user=user_data)

@app.route('/')
def hello_world():
  return "Hello world"

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000)