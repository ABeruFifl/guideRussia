from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_window():
    with open('mainWindow.html', 'r', encoding='utf-8') as html:
        return html.read()


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
