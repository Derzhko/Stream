import eventlet
import socketio


sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': './index.html'}
})


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.on('motor_command')
def motor_command(sid, data):
    print('message ', data)

    direction = data['direction']
    value = data['value']
    print(f'motor_command: {direction}  value: {value}')


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)