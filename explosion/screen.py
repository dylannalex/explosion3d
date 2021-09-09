import pygame
from random import randint, random
from explosion.constants import physics, animation


class Screen:
    def __init__(
        self,
        title: str,
        height: int,
        width: int,
        resizable: bool,
        background_color: str,
    ):
        pygame.display.set_caption(title)
        if resizable:
            self.window = pygame.display.set_mode((height, width), pygame.RESIZABLE)
        else:
            self.window = pygame.display.set_mode((height, width))
        self.background_color = background_color
        self.clear()

    def clear(self) -> None:
        self.window.fill(self.background_color)


class Particle:
    def __init__(self, radius: int, x: int, y: int, velocity: list, color: list):
        self.x = x
        self.y = y
        self.z = radius
        self.velocity = velocity
        self.color = color

    def move(self, win) -> None:
        """
        Moves the particle depending on its velocity:

        next xpos [pixels] = current xpos [pixels] + vx [pixels] * dt
        next ypos [pixels] = current ypos [pixels] + vy [pixels] * dt * -1

        Where:
        - dt = Time per frame
        - vx [pixels] = vx [meters] * CONVERSION
        - vy [pixels] = vy [meters] * CONVERSION
        """
        self.x += self.velocity[0] * animation.TPF * physics.CONVERSION
        self.y += self.velocity[1] * animation.TPF * physics.CONVERSION * -1
        self.z += self.velocity[2] * animation.TPF * physics.CONVERSION

        pygame.draw.circle(win, self.color, (self.x, self.y), self.z)


class Explosion:
    Y_LIMIT = 1000

    def __init__(
        self,
        particle_size: int,
        total_particles: int,
        x_expansion: int,
        y_expansion: int,
        win: pygame.Surface,
    ):
        self.particle_size = particle_size
        self.total_particles = total_particles
        self.x_expansion = x_expansion
        self.y_expansion = y_expansion
        self._particles = []
        self.win = win

    def set_particles(self, mx: int, my: int) -> None:
        self._particles = [
            self._create_particle(mx, my) for _ in range(self.total_particles)
        ]

    def _create_particle(self, mx, my) -> Particle:
        vx = randint(-self.x_expansion, self.x_expansion)
        vy = randint(self.y_expansion // 2, self.y_expansion)
        vz = random()

        return Particle(self.particle_size, mx, my, [vx, vy, vz], get_red_color())

    def move_particles(self) -> None:
        for particle in self._particles:
            particle.move(self.win)
            particle.velocity[1] += physics.GRAVITY * animation.TPF

            if particle.color[0] < 255:
                particle.color[0] += 1

            if particle.color[1] < 255:
                particle.color[1] += 1

            if particle.color[2] < 255:
                particle.color[2] += 1

            if particle.y > Explosion.Y_LIMIT:
                self._particles.remove(particle)


def get_red_color():
    """
    Returns a red RGB color
    """
    r = 255
    g = randint(50, 255)
    b = 0

    return [r, g, b]
