import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)

            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)

            new_radius = self.radius -  ASTEROID_MIN_RADIUS

            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = vector1
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = vector2


