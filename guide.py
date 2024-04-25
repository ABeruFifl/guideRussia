from flask import Flask, url_for, render_template, redirect, session
from flask_login import login_manager, LoginManager, login_user, login_required, logout_user

from data.forms import LoginForm, RegisterForm
from data import db_session
from data.users import User
from data.route import Route
from data.event import Event

app = Flask(__name__)
app.config['SECRET_KEY'] = 'guideRussia_secret_key'


login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def main_window():
    context = {'events': [],
               'routes': []}
    db_sess = db_session.create_session()
    for route1 in db_sess.query(Route).filter(Route.region == 'Москва').all():
        context['routes'].append(route1.get_list())
    for event1 in db_sess.query(Event).filter(Event.region == 'Москва').all():
        context['events'].append(event1.get_list())
    return render_template('main_window.html', context=context)


@app.route('/st_peterburg')
def stpeterburg():
    context = {'events': [],
               'routes': []}
    db_sess = db_session.create_session()
    for route1 in db_sess.query(Route).filter(Route.region == 'Санкт-Петербург').all():
        context['routes'].append(route1.get_list())
    for event1 in db_sess.query(Event).filter(Event.region == 'Санкт-Петербург').all():
        context['events'].append(event1.get_list())
    return render_template('main_window.html', context=context)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    context = {'proba': [list1, list2, list3]}
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', form=form)
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', form=form)
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', form=form, context=context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    context = {'proba': [list1, list2, list3]}
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form, context=context)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')


@app.route('/route/<int:route_id>')
def route(route_id):
    db_sess = db_session.create_session()
    route_list = db_sess.query(Route).filter(Route.id == route_id).first().get_list()
    return render_template('route.html', route_list=route_list)


@app.route('/event/<int:event_id>')
def event(event_id):
    db_sess = db_session.create_session()
    event_list = db_sess.query(Event).filter(Event.id == event_id).first().get_list()
    return render_template('event.html', event_list=event_list)


if __name__ == '__main__':
    db_session.global_init("db/guideRussia.sqlite3")
    app.run(port=8000, host='127.0.0.1')
