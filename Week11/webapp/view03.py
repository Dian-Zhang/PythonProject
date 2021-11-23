from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': '张三'}
    friends = [
        {'author': {'nickname': '小明'}, 'address': '福建'},
        {'author': {'nickname': '小红'}, 'address': '深圳'}
    ]
    return render_template("index03.html",
                           title="首页",
                           user=user,
                           friends=friends)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
