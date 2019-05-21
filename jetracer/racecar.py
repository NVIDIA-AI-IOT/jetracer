import traitlets


class Racecar(traitlets.HasTraits):
    steering = traitlets.Float(min=-1.0, max=1.0)
    throttle = traitlets.Float(min=-1.0, max=1.0)