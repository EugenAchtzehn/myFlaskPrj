from flask import Flask, render_template, request, redirect, url_for

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
  return render_template('form.html')

@app.route('/submit', methods=['POST', 'GET'])
def submit():
  if request.method == 'POST':
    user = request.form["user"]
    print("post: user => ", user)
    return redirect(url_for("success", name=user, action="post"))
  else:
    user = request.args.get("user")
    print("get : user => ", user)
    return redirect(url_for("success", name=user, action="get"))

@app.route("/success/<action>/<name>")
def success(name, action):
    return "{} : Welcome {} ~ !!!".format(action, name)

if __name__ == "__main__":
    app.run()