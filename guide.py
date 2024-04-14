from flask import Flask, url_for, render_template
from data import db_session

app = Flask(__name__)

list1 = ['Московский Планетарий', 'Ул. Садовая-Кудринская, д.5', 'img/planetarium.jpeg']
list2 = ['Макет космического корабля «Буран»', 'ВДНХ, Пр-т Мира, 119', 'img/buran.jpg']
list3 = ['Центр «Космонавтика и авиация»', 'ВДНХ, Пр-т Мира, 119', 'img/centerCNA.jpg']


@app.route('/')
def main_window():
    context = {'proba': [list1, list2, list3]}
    return render_template('main_window.html', context=context)


@app.route('/prob_list')
def prob_list():
    return render_template('prob_list.html')


if __name__ == '__main__':
    db_session.global_init("db/users.sqlite3")
    app.run(port=8000, host='127.0.0.1')
