from flask import Flask, render_template
import pymysql

app = Flask(__name__)


@app.route('/')
@app.route('/show')
def index():
    db = pymysql.connect(host='localhost', user='root', password='123', port=3306, db='my python final work')
    cursor = db.cursor()
    # the first is 每个时间段前二十个视频的在线人数
    sql = "select * from watch_list "
    cursor.execute(sql)
    print(cursor.rowcount)
    show = []
    for row in cursor.fetchall():
        show.append({'video_url': "https://" + row[0],
                     'video_name': row[1],
                     'video_views': row[2],
                     'video_dm': row[3],
                     'video_author': row[4],
                     'video_author_homepage': row[5],
                     'video_online_people': row[6],
                     'watch_list_id': row[7]})
    print(show)
    return render_template("show.html", title="首页", show=show)


@app.route('/hist_pic')
def hist_pic():
    return render_template("hist_pic.html", title="直方图图片展示")


@app.route('/pie_pic')
def pie_pic():
    return render_template("pie_pic.html", title="饼状图图片展示")


@app.route('/user_pic')
def user_pic():
    return render_template("user_pic.html", title="用户数据图片展示")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
