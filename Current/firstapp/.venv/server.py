from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

class Server:
    def __init__(self):
        self.start_server()
        
    def start_server(self):
        @socketio.on('connect')
        def handle_connect():
            print('Client connected')
            
        @socketio.on('disconnect')
        def handle_disconnect():
            print('Client disconnected')

        @socketio.on('message')
        def handle_message(message):
            print('Received message:', message)
            socketio.emit('message', 'Server received: ' + message)
            
if __name__ == '__main__':
    server = Server()
    socketio.run(app, host='0.0.0.0', port=5555, debug=True)