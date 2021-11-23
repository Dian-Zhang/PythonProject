# -*- encoding:utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    # 调用模板
    return render_template("index06.html", title="优化登录页面")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
