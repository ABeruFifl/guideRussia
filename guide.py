from flask import Flask, url_for, render_template, redirect
from data.forms import LoginForm, RegisterForm
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'guideRussia_secret_key'

list1 = ['Московский Планетарий', 'Ул. Садовая-Кудринская, д.5', 'img/planetarium.jpeg']
list2 = ['Макет космического корабля «Буран»', 'ВДНХ, Пр-т Мира, 119', 'img/buran.jpg']
list3 = ['Центр «Космонавтика и авиация»', 'ВДНХ, Пр-т Мира, 119', 'img/centerCNA.jpg']


@app.route('/', methods=['GET', 'POST'])
def main_window():
    form = LoginForm()
    form1 = RegisterForm()
    context = {'proba': [list1, list2, list3]}
    if form1.validate_on_submit():
        if form1.password.data != form1.password_again.data:
            return render_template('main_window.html', context=context, form=form, form1=form1)
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form1.email.data).first():
            return render_template('main_window.html', context=context, form=form, form1=form1)
        user = User(
            name=form1.name.data,
            surname=form1.surname.data,
            email=form1.email.data,
        )
        user.set_password(form1.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('main_window.html', context=context, form=form, form1=form1)


if __name__ == '__main__':
    db_session.global_init("db/guideRussia.sqlite3")
    app.run(port=8000, host='127.0.0.1')
