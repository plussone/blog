from flask import Flask, render_template, request, make_response, jsonify
import mysql
import time

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = request.args.get("name")
    time = 0
    if name is None:
        name = request.cookies.get("name", "default")
        if name != 'default' and name != -1:
            return render_template("./jump_submit.html", time=time)
    return render_template("./login.html")


@app.route('/login')
def login():
    return render_template("./login.html")


@app.route('/login_commit', methods=['GET', 'POST'])
def login_commit():
    form = request.form
    answer, uid = mysql.checking_login(form['username'], form['password'])
    response = make_response(jsonify({'message': answer}))
    response.set_cookie("name", str(uid))
    return response


@app.route('/submit')
def submit():
    localtime = time.localtime(time.time())
    date = str(localtime.tm_year) + '年' + str(localtime.tm_mon) + '月' + str(localtime.tm_mday) + '日'
    return render_template("./submit.html", time=date)


@app.route('/submit_commit', methods=['GET', 'POST'])
def submit_commit():
    form = request.form
    localtime = time.localtime(time.time())
    date = str(localtime.tm_year) + '-' + str(localtime.tm_mon).zfill(2) + '-' + str(localtime.tm_mday).zfill(2)
    mysql.add_data(date, form['math'], form['english'], form['specialty'], form['politics'], form['vocabulary'], form['spoken'], form['hearing'], form['remarks'])
    response = make_response(jsonify({'message': 1}))
    return response


if __name__ == '__main__':
    app.run()
