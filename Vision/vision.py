from picamera import PiCamera
import time

class Vision(PiCamera):
    def __init__(self):
        super().__init__()
        
        self.resolution = (1200, 1200)
        self.shutter_speed = 10000

        self.status = 'Disabled'
    
    def take_picture(self):
        self.start_preview()
        self.capture('./Vision/vision.jpg')

    def vision(self):
        while self.status == 'Enabled':
            self.take_picture()

v = Vision()
v.take_picture()