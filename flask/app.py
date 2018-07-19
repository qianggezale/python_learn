from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '你好！'

@app.route('/hello')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()