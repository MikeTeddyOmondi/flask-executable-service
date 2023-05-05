from waitress import serve
from flask import Flask
import logging

app = Flask(__name__)

# Disable Flask's console logging
log = logging.getLogger('werkzeug')
log.propagate = False


@app.route('/')
def hello():
    return 'Running background service!'


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
