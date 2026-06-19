import numpy as np

class Body:
    def __init__(self, x, y, z, mass, vx=0, vy=0, vz=0):
        self.position = np.array([x, y, z], dtype=float)
        self.velocity = np.array([vx, vy, vz], dtype=float)
        self.mass = mass

    def update(self, force, dt):
        acceleration = force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt