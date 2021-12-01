from flask import Flask

app = Flask(__name__)


@app.route('/')
def test():
    return "Hello Flask"


@app.route('/index')
def test2():
    return "hello index"


@app.route('/user/')
def test3():
    return "hello user"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
