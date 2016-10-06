import datetime

import flask


app = flask.Flask('tracker')


users = {}


@app.route('/join', methods=['POST'])
def _join():
    data = flask.request.get_json()
    users[flask.request.remote_addr] = {
        'name': data['name'],
        'ip': flask.request.remote_addr,
        'joined_at': datetime.datetime.now(),
    }
    return "OK"


@app.route('/users')
def _users():
    return flask.jsonify(list(users.values()))


app.run('0.0.0.0')
