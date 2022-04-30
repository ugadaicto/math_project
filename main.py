from flask import Flask, url_for, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from forms.quiz_form import QuizForm
import sqlite3

print('a')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'rabotai_pozhaluysta'
USER_LOGGED_IN = False
LOGIN = None


def password_is_correct(user_name, password):
    con = sqlite3.connect('profiles.db')
    cur = con.cursor()
    result = cur.execute(f"""SELECT password FROM profiles WHERE user_name = '{user_name}'""")
    result = result.fetchall()
    if result:
        return result[0][0] == password
    return False


def make_new_profile(user_name, password):
    con = sqlite3.connect('profiles.db')
    cur = con.cursor()
    cur.execute(
        f"""INSERT INTO profiles(user_name, password, tasks_solved, tasks_solved_correctly)
         VALUES('{user_name}', '{password}', 0, 0)""")
    con.commit()


@app.route('/login', methods=['GET', 'POST'])
def login():
    global USER_LOGGED_IN
    global LOGIN
    form = LoginForm()
    if form.validate_on_submit():
        login, password = form.username._value(), form.password._value()

        if password_is_correct(login, password):
            USER_LOGGED_IN = True
            LOGIN = login
            return render_template('menu.html', user_logged_in=USER_LOGGED_IN)

        else:
            return render_template('log.html', title='Авторизация', form=form, custom_error="Неверный логин или пароль")

    return render_template('log.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    global USER_LOGGED_IN
    global LOGIN
    form = RegisterForm()
    if form.validate_on_submit():
        user_name, password, password_check = form.username._value(), form.password._value(), form.password_check._value()

        if password != password_check:
            return render_template('reg.html', title='Регистрация', form=form,
                                   custom_error="Введнные пароли не сходятся")

        make_new_profile(user_name, password)
        USER_LOGGED_IN = True
        LOGIN = user_name
        return render_template('menu.html', user_logged_in=USER_LOGGED_IN)

    return render_template('reg.html', title='Регистрация', form=form)


@app.route('/')
def menu():
    global USER_LOGGED_IN
    return render_template('menu.html', user_logged_in=USER_LOGGED_IN)


@app.route("/lesson_1")
def lesson_1():
    return render_template("lesson.html", title='test', lesson_text='lol')


@app.route("/lesson_2")
def lesson_2():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_3")
def lesson_3():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_4")
def lesson_4():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_5")
def lesson_5():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_6")
def lesson_6():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_7")
def lesson_7():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_8")
def lesson_8():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_9")
def lesson_9():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_10")
def lesson_10():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_11")
def lesson_11():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_12")
def lesson_12():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_13")
def lesson_13():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_14")
def lesson_14():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_15")
def lesson_15():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_16")
def lesson_16():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_17")
def lesson_17():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_18")
def lesson_18():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_19")
def lesson_19():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_20")
def lesson_20():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_21")
def lesson_21():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_22")
def lesson_22():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_23")
def lesson_23():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_24")
def lesson_24():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_25")
def lesson_25():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_26")
def lesson_26():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_27")
def lesson_27():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_28")
def lesson_28():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_29")
def lesson_29():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_30")
def lesson_30():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_31")
def lesson_31():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_32")
def lesson_32():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_33")
def lesson_33():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_34")
def lesson_34():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_35")
def lesson_35():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_36")
def lesson_36():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_37")
def lesson_37():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_38")
def lesson_38():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_39")
def lesson_39():
    return render_template("lesson.html", title="", text_lesson="")


@app.route("/lesson_40")
def lesson_40():
    return render_template("lesson.html", title="", text_lesson="")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
