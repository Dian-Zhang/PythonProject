from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': '张三'}
    return render_template("index01.html", title="首页", user=user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
