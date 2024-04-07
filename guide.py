from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def main_window():
    return render_template('mainWindow.html')


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
