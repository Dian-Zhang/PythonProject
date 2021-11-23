from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    # 调用模板
    return render_template("index04.html", title="登陆页面")


@app.route('/login_post', methods=['POST'])
def loginop():
    if request.method == 'POST':
        name = request.form.get("username", "用户不存在")
        pwd = request.form.get("password", "密码不存在")
        print("********************")
        print(name)
        print(pwd)
        if name == "admin" and pwd == "123456":
            return '<h1>你好，%s<h1>' % name
        else:
            return render_template("index04.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
