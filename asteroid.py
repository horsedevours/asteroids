from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        newV1 = self.velocity.rotate(angle)
        newV2 = self.velocity.rotate(-angle)
        newRadius = self.radius - ASTEROID_MIN_RADIUS

        ast1 = Asteroid(self.position.x, self.position.y, newRadius)
        ast1.velocity = 1.2 * newV1
        ast2 = Asteroid(self.position.x, self.position.y, newRadius)
        ast2.velocity = 1.2 * newV2