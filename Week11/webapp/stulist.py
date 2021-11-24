from flask import Flask, render_template, request, g

import os
from SQLiteOp import connect_db

app = Flask(__name__)


# 请求之前被调用
@app.before_request
def before_request():
    g.db = connect_db()


# 响应后被调用
@app.teardown_request
def teardowm_request(exception):
    g.db.close()


@app.route('/')
@app.route('/index')
def index():
    sqlstr = 'select * from stus'
    cur = g.db.execute(sqlstr)
    stus = []
    for row in cur.fetchall():
        print(row[0], row[1], row[2])
        dic = dict(no=row[1], name=row[2])
        stus.append(dic)
    print('stus', stus)
    # 调用模板
    return render_template("stulist.html", title="学生列表", stus=stus)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
