from jetmotor import Motor
import traitlets


class Racecar(traitlets.HasTraits):
    image = traitlets.Any()
    steering = traitlets.Float(min=-1.0, max=1.0)
    throttle = traitlets.Float(min=-1.0, max=1.0)