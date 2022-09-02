from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello():
    return render_template('hello.html')

@app.route('/home')
def home():
  return render_template('home.html')

# render_template 第二個參數可以附帶資料內容
@app.route('/page')
def page():
  return render_template('page.html', text="Python Flask!")

@app.route('/page/app')
def pageAppInfo():
  # dict
  appInfo = {
    'id': 5,
    'name': 'Python - Flask',
    'version': '99.0.0',
    'author': 'Eugene',
    'remark': 'Python - Web Framework'
  }
  return render_template('page.html', appInfo=appInfo)