import socketio
import time    
import base64
import cv2


class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class SIOClient(Singleton):
    
    sio = socketio.Client()

          
    def setup(self, addrs, fps):

        self.period = 1/fps
        self.last_emit_t = time.time()
        
        SIOClient.sio.connect(addrs, transports=['polling'], namespaces=['/car'])
        time.sleep(1)

    @sio.on('connect', namespace='/car')
    def connect():
        print('connected to server')

    @sio.on('connect_error', namespace='/car')
    def connect_error(x):
        print('failed to connect to server')

    @sio.on('disconnect', namespace='/car')
    def disconnect():
        print('disconnected from server.')

    @staticmethod
    def _convert_image_to_jpeg(image):
        frame = cv2.imencode('.jpg', image)[1].tobytes()
        frame = base64.b64encode(frame).decode('utf-8')
        return "data:image/jpeg;base64,{}".format(frame)

        
    def send_data(self, frame):
        current_t = time.time()

        if current_t - self.last_emit_t > self.period:
            self.last_emit_t = current_t
            SIOClient.sio.emit('car2server',
                               {'image': SIOClient._convert_image_to_jpeg(frame) },
                               namespace='/car')
