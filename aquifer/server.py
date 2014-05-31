import flask


app = flask.Flask(__name__)

CURRENT_LEVEL = {
    "timestamp": "2014-05-31T12:00:00Z",
    "level": 642.56,
    "average": 642.56
}


@app.route('/level')
def current_level():
    return flask.jsonify(level=CURRENT_LEVEL)


if __name__ == '__main__':
    app.run()
