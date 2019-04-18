from jetmotor import Motor
import traitlets


class Racecar(traitlets.HasTraits):
    steering_motor = traitlets.Instance(klass=Motor)
    throttle_motor = traitlets.Instance(klass=Motor)