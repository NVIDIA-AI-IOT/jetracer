from .racecar import Racecar
import traitlets
from adafruit_servokit import ServoKit
from jetmotor.adafruit_servokit_motor import AdafruitServoKitMotor


class DefaultRacecar(Racecar):
    def __init__(self, *args, **kwargs):
        kit = ServoKit(channels=16)
        self.steering_motor = AdafruitServoKitMotor(kit=kit, channel=0)
        self.throttle_motor = AdafruitServoKitMotor(kit=kit, channel=1, alpha=-1.0)