from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/data')
def sensor_data():
    sid = request.args.get('sid')
    value = request.args.get('value')
    return f"SID: " + 2* (sid) + ", Value: " + 2*value


if __name__ == '__main__':
    app.run()
