import config

from flask import Flask
from flask_sslify import SSLify


app = Flask(__name__, static_url_path='')

sslify = SSLify(app)


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
