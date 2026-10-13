import pygame
from pygame import Surface

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import random
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        rand_angle = random.uniform(20, 50)
        rot_1 = pygame.math.Vector2(rand_angle)
        rot_2 = pygame.math.Vector2(-rand_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_ast_1.velocity = pygame.Vector2(rot_1 * 1.2)
        new_ast_2.velocity = pygame.Vector2(rot_2 * 1.2)
