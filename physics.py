import numpy as np
from constants import G

def gravitational_force(body1, body2):

    r = body2.position - body1.position
    distance = np.linalg.norm(r)

    if distance == 0:
        return np.zeros(3)

    force_mag = G * body1.mass * body2.mass / distance**2

    return force_mag * r / distance