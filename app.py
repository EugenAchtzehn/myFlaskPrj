from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect, url_for, jsonify
import json

# 約定俗成用法，讓 flask 知道你的 root 在哪裡
app = Flask(__name__)

# @app.route("path") 後接的一定是一個要執行的 function
# 讓路由知道要執行哪個工作
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

@app.route('/page/data')
def pageData():
  # dict
  data = {
    '01': 'Text111',
    '02': 'Text222',
    '03': 'Text333',
    '04': 'Text444',
    '05': 'Text555',
  }
  return render_template('page.html', data=data)

# 在模板頁面中引入 js, css
@app.route('/static')
def staticPage():
  return render_template('static.html')

@app.route('/form')
def formPage():
  # 表單頁
  return render_template('form.html')

# 對 /submit 路徑接收 POST, GET 方法
@app.route('/submit', methods=['POST', 'GET'])
def submit():
  # 如果請求方法為 post，呼叫 request 物件下的 method 可知前端用 HTTP 哪種方法
  if request.method == 'POST':
    # post 方法必須使用 request.form 的變數
    user = request.form["user"]
    print("post: user => ", user)
    # 重導向到成功頁
    return redirect(url_for("success", name=user, action="post"))
  else:
    # get 方法必須使用 request.args 的變數
    user = request.args.get("user")
    print("get : user => ", user)
    # redirect() 函式包含 url_for() 函式，是固定用法
    return redirect(url_for("success", name=user, action="get"))

@app.route("/success/<action>/<name>")
def success(name, action):
    # 字串帶入 action, name
    # 下面是 demo
    # return "{} : Welcome {} ~ !!!".format(action, name)
    return f"{action} : Welcome {name} ~ !!!"

# ajax testing
@app.route("/apitest")
def webapi():
  return render_template('data.html')

if __name__ == "__main__":
  # debug 模式允許 auto reload for code changes
  # And show a debugger in case an exception happened.
  app.run(debug=True)
  # app.run()