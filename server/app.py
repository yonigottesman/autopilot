from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route("/")
def hello_world():
    return render_template('index.html')


@socketio.on('connect', namespace='/web')
def connect_web():
    print('web connected')


@socketio.on('disconnect', namespace='/web')
def disconnect_web():
    print('web disconnect')



@socketio.on('connect', namespace='/car')
def connect_cv():
    print('car connected')


@socketio.on('disconnect', namespace='/car')
def disconnect_cv():
    print('car disconnected')


@socketio.on('car2server', namespace='/car')
def handle_cv_message(message):
    socketio.emit('server2web', message, namespace='/web')


if __name__ == "__main__":
    socketio.run(app=app, host="0.0.0.0", port=5000, debug=True)
