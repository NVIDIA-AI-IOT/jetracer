from .racecar import Racecar
import traitlets
from adafruit_servokit import ServoKit
from jetmotor.adafruit_servokit_motor import AdafruitServoKitMotor
from jetcam.imx219 import IMX219


class DefaultRacecar(Racecar):
    def __init__(self, *args, **kwargs):
        kit = ServoKit(channels=16)
        self.camera = IMX219(capture_width=1280, capture_height=720, fps=30, width=224, height=224)
        self.steering_motor = AdafruitServoKitMotor(kit=kit, channel=0)
        self.throttle_motor = AdafruitServoKitMotor(kit=kit, channel=1)
        
        # link camera
        traitlets.link((self.camera, 'value'), (self, 'image'))
        
        # link throttle
        traitlets.dlink((self, 'throttle'), (self.throttle_motor, 'value'), transform=lambda x: -x)
        traitlets.dlink((self.throttle_motor, 'value'), (self, 'throttle'), transform=lambda x: -x)
        
        # link steering
        traitlets.link((self, 'steering'), (self.steering_motor, 'value'))