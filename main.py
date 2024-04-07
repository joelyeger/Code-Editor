from website import create_app

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = create_app()
socketio = SocketIO(app)

connected_clients = 0


@socketio.on('connect')
def handle_connect():
    global connected_clients
    connected_clients += 1
    if connected_clients == 1:
        emit('mode', {'mode': 'read_only'})
    else:
        emit('mode', {'mode': 'read_write'})


@socketio.on('disconnect')
def handle_disconnect():
    global connected_clients
    connected_clients -= 1


@socketio.on('text_update')
def handle_text_update(data):
    text = data['text']
    emit('update_text', {'text': text}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)