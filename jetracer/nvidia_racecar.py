from .racecar import Racecar
import traitlets
from adafruit_servokit import ServoKit
from jetmotor.adafruit_servokit_motor import AdafruitServoKitMotor
from jetcam.imx219 import IMX219


class NvidiaRacecar(Racecar):
    def __init__(self, *args, **kwargs):
        kit = ServoKit(channels=16)
        self.steering_motor = AdafruitServoKitMotor(kit=kit, channel=0)
        self.throttle_motor = AdafruitServoKitMotor(kit=kit, channel=1)
        
        # link throttle
        traitlets.dlink((self, 'throttle'), (self.throttle_motor, 'value'), transform=lambda x: -x)
        traitlets.dlink((self.throttle_motor, 'value'), (self, 'throttle'), transform=lambda x: -x)
        
        # link steering
        traitlets.link((self, 'steering'), (self.steering_motor, 'value'))