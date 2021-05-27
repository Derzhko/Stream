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
    delta = 0
    direction = data['direction']
    value = data['value']
    if direction == 'left':
        delta -= int(value)
    elif direction == 'right':
        delta += int(value)
    print(f'motor_command: {direction}  value: {value}  delta: {delta}')

@sio.on('generator_type_of_signal')
def type_of_signal(sid, data):
    print('message ', data)
    type_of_signal = data['typeofSignal']
    print(f'generator type of signal {type_of_signal}')

@sio.on('generator_set_frequency')
def set_frequency(sid, data):
    print('message', data)
    value = data['value']
    size = data['size']
    print(f'generator set frequency  value: {value}  size {size}')

@sio.on('generator_set_amplitude')
def set_amplitude(sid, data):
    print('message', data)
    value = data['value']
    print(f'generator set amplitude  value {value}')


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    delta = 0
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)