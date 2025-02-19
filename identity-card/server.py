from flask import Flask
from flask import render_template



app = Flask(__name__)


@app.route('/')
def index(name=None):
    return render_template('index.html',name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
