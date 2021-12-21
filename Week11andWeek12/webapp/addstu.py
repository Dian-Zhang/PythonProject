from flask import Flask, render_template, request, g, redirect, url_for

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
@app.route('/addpage')
def index():
    # 调用模板
    return render_template("addstu.html", title="增加页面")


# 学生展示列表
@app.route('/stupage')
def stushow():
    sqlstr = 'select * from stus'
    cur = g.db.execute(sqlstr)
    stus = []
    for row in cur.fetchall():
        print(row[0], row[1], row[2])
        dic = dict(no=row[1], name=row[2])
        stus.append(dic)
    # print('stus',stus)
    return render_template("stulist.html", title="学生列表", stus=stus)


@app.route('/add_stu', methods=['POST'])
def add():
    if request.method == 'POST':
        id = request.form.get("id", "用户不存在")
        no = request.form.get("no", "密码不存在")
        name = request.form.get("name", "密码不存在")
        # print(id,no,name)
        sqlstr = 'insert into  stus(STU_ID,STU_NO,STU_NAME) values (?,?,?)'
        g.db.execute(sqlstr, [id, no, name])
        g.db.commit()
        # return '<h1>插入成功</h1>'
        # 对应展示功能的函数，不是路由
        return redirect(url_for('stushow'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
