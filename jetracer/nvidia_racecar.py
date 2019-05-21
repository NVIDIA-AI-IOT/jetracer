from .racecar import Racecar
import traitlets
from adafruit_servokit import ServoKit


class NvidiaRacecar(Racecar):
    
    i2c_address = traitlets.Integer(default_value=0x40)
    steering_channel = traitlets.Integer(default_value=0)
    throttle_channel = traitlets.Integer(default_value=1)
    
    def __init__(self, i2c_addres=0x40, steering_channel=0, throttle_channel=1):
        super(NvidiaRacecar, self).__init__(*args, **kwargs)
        self.kit = ServoKit(channels=16, address=self.i2c_address)
        self.steering_motor = self.kit.continuous_servo[self.steering_channel]
        self.throttle_motor = self.kit.continuous_servo[self.throttle_channel]
    
    @traitlets.observe('steering')
    def _on_steering(self, change):
        self.steering_motor.throttle = change['new']
    
    @traitlets.observe('throttle')
    def _on_throttle(self, change):
        self.throttle_motor.throttle = change['new']