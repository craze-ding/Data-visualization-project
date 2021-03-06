from flask import Flask
from flask import render_template
from flask import jsonify
from jieba.analyse import extract_tags
import utils

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('main.html')


@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm": int(data[0]), "suspect": int(data[1]), "heal": int(data[2]), "dead": int(data[3])})


@app.route('/c2')
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        res.append({"name": tup[0], "value": int(tup[1])})
    return jsonify({"data": res})


@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    day, confirm, suspect, heal, dead = [], [], [], [], []
    for a, b, c, d, e in data[7:]:  # 很多卫健委网站前7天都是没有数据的，所以把前7天砍掉了
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day": day, "confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})


@app.route("/l2")
def get_l2_data():
    data = utils.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})


@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k, v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})


@app.route("/r2")
def get_r2_data():
    data = utils.get_r2_data()  # 格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
    # print(data)
    d = []
    for i in data:
        # k = i[0].rstrip(string.digits)  # 移除热搜数字
        # v = i[0][len(data):]  # 获取热搜数字
        v = i[0].split("\n")[1]
        # print(v)
        # ks = extract_tags(i[0])  # 使用jieba 提取关键字
        ks = extract_tags(i[0].split("\n")[3])  # 使用jieba 提取关键字
        # print(ks)
        for j in ks:
            if not j.isdigit():
                d.append({"name": j, "value": v})
    return jsonify({"kws": d})


@app.route('/time')
def gettime():
    return utils.get_time()


@app.route('/tem')
def hello_world3():
    return render_template("main.html")


@app.route('/ajax', methods=["get", "post"])
def hello_world4():
    return '10000'


if __name__ == '__main__':
    # app.run(host='xxx.xxx.xxx.xxx',port=8080)
    app.run()
    # app.run(host='0.0.0.0')
